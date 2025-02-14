from fasthtml.common import HighlightJS, fast_app

hdrs = (HighlightJS(langs=["python", "javascript", "html", "css"]),)
app, rt = fast_app(hdrs=hdrs)
