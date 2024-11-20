import openai
import os

openai.api_key = "api_key"

def read_article(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

def process_article_with_openai(article_text):
    prompt = (
        "Jesteś specem od kodowania. Przerób poniższy tekst na kod HTML, spełniając następujące wytyczne:"
"1. Użyj odpowiednich tagów HTML do strukturyzacji treści, takich jak <h1>, <h2>, <p>, <ul>, <ol>, <strong>, <em>, aby poprawnie oddać strukturę logiczną artykułu."
"2. Wstaw pare zdjęć w miejscach, gdzie mogą być ona pomocne dla wizualizacji treści. Do tego celu użyj tagu <img> z następującymi atrybutami:"
"- src=\"image_placeholder.jpg\" jako miejsce na obrazek."
"- alt: Wartość atrybutu 'alt' powinna zawierać tekstowy prompt do wygenerowania grafiki, którą umieszczamy w danym miejscu. Treść promptu powinna uwzględniać szczegóły, takie jak: temat obrazu, styl wizualny, istotne elementy graficzne i powiązanie z sekcją artykułu."
"3. Pod każdym obrazkiem umieść krótki opis dodanej grafiki z użyciem <figcaption>."
"4. Wygenerowany kod HTML powinien zawierać wyłącznie zawartość do umieszczenia pomiędzy tagami <body> i </body>."
"5. Nie dołączaj znaczników <html>, <head> ani <body>."
"6. Nie dodawaj żadnego kodu CSS ani JavaScript."
"Oto tekst artykułu:\n\n" + article_text
    )

    response = openai.Completion.create(
    engine="gpt-3.5-turbo-instruct",
    prompt=prompt,
    max_tokens=1600,
    temperature=0.7
    )
    return response.choices[0].text.strip()

def save_html_file(file_path, html_content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)

def create_template():
    template_html = """
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Podgląd Artykułu</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {
                font-family: 'Roboto', sans-serif;
                line-height: 1.8;
                margin: 20px;
                background: linear-gradient(135deg, #e0f7fa, #fff);
                color: #212529;
            }
            h1 {
                color: #007bff;
                text-align: center;
                font-size: 2.5em;
                margin-bottom: 20px;
                text-shadow: 1px 1px 2px #ccc;
            }
            h2 {
                color: #17a2b8;
                border-left: 5px solid #17a2b8;
                padding-left: 10px;
                margin-top: 20px;
                margin-bottom: 10px;
            }
            p {
                font-size: 1.1em;
                text-align: justify;
                margin-bottom: 15px;
            }
            img {
                display: block;
                max-width: 90%;
                height: auto;
                margin: 20px auto;
                border: 5px solid #17a2b8;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
            }
            figcaption {
                text-align: center;
                font-size: 0.9em;
                color: #6c757d;
                font-style: italic;
                margin-top: -10px;
            }
            ul {
                padding-left: 20px;
            }
            ul li {
                margin-bottom: 10px;
                color: #343a40;
            }
            footer {
                text-align: center;
                margin-top: 40px;
                font-size: 0.9em;
                color: #6c757d;
            }
        </style>
    </head>
    <body>
    </body>
    </html>
    """
    with open("szablon.html", "w", encoding="utf-8") as file:
        file.write(template_html)


def create_preview(article_html):
    preview_html = f"""
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Podgląd Artykułu</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            body {{
                font-family: 'Roboto', sans-serif;
                line-height: 1.8;
                margin: 20px;
                background: linear-gradient(135deg, #e0f7fa, #fff);
                color: #212529;
            }}
            h1 {{
                color: #007bff;
                text-align: center;
                font-size: 2.5em;
                margin-bottom: 20px;
                text-shadow: 1px 1px 2px #ccc;
            }}
            h2 {{
                color: #17a2b8;
                border-left: 5px solid #17a2b8;
                padding-left: 10px;
                margin-top: 20px;
                margin-bottom: 10px;
            }}
            p {{
                font-size: 1.1em;
                text-align: justify;
                margin-bottom: 15px;
            }}
            img {{
                display: block;
                max-width: 90%;
                height: auto;
                margin: 20px auto;
                border: 5px solid #17a2b8;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
            }}
            figcaption {{
                text-align: center;
                font-size: 0.9em;
                color: #6c757d;
                font-style: italic;
                margin-top: -10px;
            }}
            ul {{
                padding-left: 20px;
            }}
            ul li {{
                margin-bottom: 10px;
                color: #343a40;
            }}
            footer {{
                text-align: center;
                margin-top: 40px;
                font-size: 0.9em;
                color: #6c757d;
            }}
        </style>
    </head>
    <body>
        {article_html}
    </body>
    </html>
    """
    with open("podglad.html", "w", encoding="utf-8") as file:
        file.write(preview_html)


def main():
    input_file = "artykul.txt"
    output_file = "artykul.html"
    
    if not os.path.exists(input_file):
        print(f"Plik {input_file} nie istnieje.")
        return

    print("Odczytuję artykuł...")
    article_text = read_article(input_file)

    print("Przetwarzam artykuł z wykorzystaniem OpenAI...")
    html_content = process_article_with_openai(article_text)

    print("Zapisuję wynikowy HTML do pliku...")
    save_html_file(output_file, html_content)

    print("Tworzę szablon HTML w szablon.html...")
    create_template()

    print("Tworzę podgląd artykułu w podglad.html...")
    create_preview(html_content)

    print(f"Zadanie zakończone.")

if __name__ == "__main__":
    main()