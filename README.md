# BWSDataset.github.io
This is a Bangla text summarization tool hosted on [bwsdataset.github.io](https://bwsdataset.github.io/). It utilizes pretrained large language models (LLMs) to generate concise and meaningful summaries of Bangla text. The tool is built on top of state-of-the-art multilingual T5 models and is designed to support researchers, students, and professionals working with Bangla language processing.

## Features
- Supports Bangla text summarization using state-of-the-art pretrained models.
- Powered by the **multilingual T5 model**, which achieved the best performance in our experiments.
- Provides an intuitive **Gradio interface** for easy text input and summary generation.
- Hosted as a web-based application for easy accessibility.

## Dataset
This tool was developed as part of research that introduced the [**BWSD dataset**](https://zenodo.org/records/14702674)—a novel Bangla summarization dataset. The dataset was constructed by collecting Bangla articles from diverse sources, preprocessing them using the custom [**Readiness Tool**](https://github.com/BWSDataset/readiness), and generating summaries with human annotators and automatic models.

## How It Works
1. Users input Bangla text into the provided text box.
2. The tool processes the text using the **mT5 model** to generate an abstractive summary.
3. The generated summary is displayed for the user.

## Usage
Visit [bwsdataset.github.io](https://bwsdataset.github.io/) and input your Bangla text to generate an automatic summary.

## Technologies Used
- **Flask**: Backend framework for hosting the web service.
- **Gradio**: Interactive UI for summarization.
- **Google Drive API**: For loading and processing dataset.
- **Pretrained LLMs**: BanglaT5, BanglaBERT, and multilingual T5.

## License
This project is licensed under the **MIT License**.

---
Developed as part of the research on Bangla text summarization.
