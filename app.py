import streamlit as st
from pdf_utils import extract_text_with_pages, chunk_text_with_pages
from summarizer import generate_summary
from qa import embed_texts, answer_question

@st.cache_data
def compute_embeddings(texts):
    return embed_texts(texts)

st.set_page_config(page_title="Research Paper Assistant", layout="wide")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "summary" not in st.session_state:
    st.session_state["summary"] = None

if "chunks" not in st.session_state:
    st.session_state["chunks"] = None

if "embeddings" not in st.session_state:
    st.session_state["embeddings"] = None

st.title("📄 Research Paper Assistant")

uploaded_file = st.file_uploader("Upload a research paper (PDF)", type="pdf")

if uploaded_file:
    st.success("PDF uploaded successfully!")

    if st.button("Generate Summary"):
        with st.spinner("Reading and summarizing..."):
            try:
                pages = extract_text_with_pages(uploaded_file)
                full_text = " ".join([p["text"] for p in pages])

                summary = generate_summary(full_text)
                st.session_state["summary"] = summary

                chunks = chunk_text_with_pages(pages)
                embeddings = compute_embeddings([c["text"] for c in chunks])

                st.session_state["chunks"] = chunks
                st.session_state["embeddings"] = embeddings
                st.session_state["messages"] = []

            except Exception as e:
                st.error(f"Something went wrong: {e}")

if st.session_state["summary"]:
    st.subheader("📌 Summary")
    st.markdown(st.session_state["summary"])
    st.divider()

if st.session_state["chunks"]:
    st.subheader("💬 Chat with your paper")

    for msg in st.session_state["messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Ask a question about the paper...")

    if user_input:
        st.session_state["messages"].append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    answer = answer_question(
                        user_input,
                        st.session_state["chunks"],
                        st.session_state["embeddings"]
                    )
                    st.markdown(answer)
                    st.session_state["messages"].append({
                        "role": "assistant",
                        "content": answer
                    })
                except Exception as e:
                    st.error(f"Something went wrong: {e}")