from docx.enum.text import WD_COLOR_INDEX

for paragraph in document.paragraphs:
    if 'vehicle' in paragraph.text:
        for run in paragraph.runs:
            if 'vehicle' in run.text:
                x = run.text.split('vehicle')
                run.clear()
                for i in range(len(x)-1):
                    run.add_text(x[i])
                    run.add_text('vehicle')
                    run.font.highlight_color = WD_COLOR_INDEX.YELLOW
