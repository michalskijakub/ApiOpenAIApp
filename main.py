import openai
import os

openai.api_key = "API_Key"

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
    max_tokens=1500,
    temperature=0.7
    )
    return response.choices[0].text.strip()

def save_html_file(file_path, html_content):
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(html_content)

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

    print(f"Zadanie zakończone. Wynik zapisano w pliku {output_file}.")

if __name__ == "__main__":
    main()