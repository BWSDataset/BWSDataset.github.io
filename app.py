import gradio as gr
from transformers import pipeline
from articles import *

def summarise(text, max_length=130, min_length=30, model_path='google/mt5-base'):
    summarizer = pipeline("summarization", model=model_path, tokenizer=model_path)

    result = summarizer(text, max_length=int(max_length), min_length=int(min_length))
    summary = result[0]['summary_text']
    return summary

# Gradio UI
demo = gr.Blocks()
with demo:
    gr.Markdown("# Bangla Text Summarization with Pre-trained mT5 Model")
    gr.Markdown("### আপনি যেই তথ্য সংক্ষেপ করতে চান সেটি প্রদান করুন অথবা উদাহরণ হিসেবে দেওয়া যেকোনো একটি তথ্য নির্বাচন করুন")

    with gr.Tabs():
        with gr.TabItem("উদাহারণসমূহঃ"):
            with gr.Column():
                rad = gr.Radio(['উদাহারণ ১', 'উদাহারণ ২', 'উদাহারণ ৩'], label='তথ্য নির্বাচন করুন')
                text1 = gr.Textbox(label='উদাহারণ', interactive=False)
                rad2 = gr.Radio(['mT5 মডেল'], label='সংক্ষেপকরার মডেল')
                max1 = gr.Slider(25, 135, 60, label='সংক্ষিপ্ত তথ্যের সর্বোচ্চ দৈর্ঘ্য')
                min1 = gr.Slider(25, 135, 30, label='সংক্ষিপ্ত তথ্যের সর্বনিম্ন দৈর্ঘ্য')
            submit1 = gr.Button('সংক্ষিপ্ত করুন')

        with gr.TabItem("নতুন তথ্য সংক্ষেপকরনঃ"):
            with gr.Column():
                text2 = gr.Textbox(label='আপনার তথ্য প্রদান করুন')
                rad3 = gr.Radio(['mT5 মডেল'], label='সংক্ষেপকরার মডেল')
                max2 = gr.Slider(25, 135, 60, label='সংক্ষিপ্ত তথ্যের সর্বোচ্চ দৈর্ঘ্য')
                min2 = gr.Slider(25, 135, 30, label='সংক্ষিপ্ত তথ্যের সর্বনিম্ন দৈর্ঘ্য')
            submit2 = gr.Button('সংক্ষিপ্ত করুন')

    # Update example text
    def action1(choice):
        articles = {
            'উদাহারণ ১': article_1,
            'উদাহারণ ২': article_2,
            'উদাহারণ ৩': article_3
        }
        return articles.get(choice, "")

    rad.change(action1, inputs=rad, outputs=[text1])
    op = gr.Textbox(label='সংক্ষিপ্ত তথ্য', interactive=False)

    model_path = "C:\\Users\\avish\\Downloads\\Text-Summarisation\\saved_model"

    def fn(hidden_text, max_length, min_length):
    
        return summarise(hidden_text, max_length, min_length, model_path)
    
    submit1.click(fn=fn, inputs=[text1, max1, min1], outputs=[op])
    submit2.click(fn=fn, inputs=[text2, max2, min2], outputs=[op])

demo.queue()
demo.launch(share=True, pwa=True)
