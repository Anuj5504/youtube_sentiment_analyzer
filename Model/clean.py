import nbformat

input_path = "youtube_sentiment.ipynb"           # <-- Replace with downloaded filename
output_path = "youtube_sentiment_model.ipynb"  # <-- This will be the cleaned file

def clean_widgets_from_notebook(input_path, output_path):
    nb = nbformat.read(input_path, as_version=4)

    # Remove 'widgets' from each cell's metadata
    for cell in nb.cells:
        if "metadata" in cell and "widgets" in cell["metadata"]:
            del cell["metadata"]["widgets"]

    # Remove global widget metadata
    if "widgets" in nb.get("metadata", {}):
        del nb["metadata"]["widgets"]

    # Save the cleaned notebook
    nbformat.write(nb, output_path)
    print(f"✅ Cleaned notebook saved as '{output_path}'")

clean_widgets_from_notebook(input_path, output_path)
