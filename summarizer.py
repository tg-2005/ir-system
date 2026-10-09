from transformers import pipeline

_summarizer = None

def get_summarizer():
    global _summarizer
    if _summarizer is None:
        try:
            _summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
        except Exception as e:
            print("Summarizer warning (using abstract fallback):", e)
            _summarizer = False
    return _summarizer

def summarize_text(text, max_length=300, min_length=50):
    if not text or len(text.strip()) < min_length:
        return text
    
    sum_pipe = get_summarizer()
    if sum_pipe:
        try:
            input_text = text[:1024]
            max_len = min(max_length, len(input_text.split()))
            min_len = min(min_length, max_len // 2)
            if max_len > min_len and min_len > 10:
                res = sum_pipe(input_text, max_length=max_len, min_length=min_len, do_sample=False)
                return res[0]['summary_text']
        except Exception as e:
            print("Summarization fallback due to:", e)
    
    # Clean fallback: concise key points from abstract
    sentences = [s.strip() for s in text.replace("\n", " ").split('. ') if s.strip()]
    return '. '.join(sentences[:3]) + ('.' if sentences and not sentences[min(2, len(sentences)-1)].endswith('.') else '')
