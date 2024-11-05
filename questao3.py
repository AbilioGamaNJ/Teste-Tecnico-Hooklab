from seleniumwire import webdriver
from seleniumwire.utils import decode as decodesw
import json


def show_request_urls(driver, target_url):
    driver.get(target_url)
    urls = []
    for request in driver.requests:
        urls.append({"url": request.url})
    return urls


def show_response(driver, target_url):
    driver.get(target_url)
    resps = []

    for request in driver.requests:
        try:
            data = decodesw(
                request.response.body,
                request.response.headers.get("Content-Encoding","identity")
            )
            resp = json.loads(data.decode("utf-8"))
            resps.append(resp)
        except:
            pass
    return resps

def main():
    keywords = ["proxytown"]
    driver = webdriver.Firefox(seleniumwire_options={"disabled_encoding": True})
    target_url = "https://magazineluiza.com.br/smartphone-samsung-galaxy-a15-65-128gb-azul-claro-4g-4gb-ram-cam-tripla-50mp-selfie-13mp-5000mah-dual-chip/p/237216300/te/ga15/"

    urls = show_request_urls(driver, target_url)
    resps = show_response(driver, target_url)

    for url in urls:
        for kw in keywords:
          if kw in url["url"]:
            print(url)

    with open('data.json', 'w') as f:
        json.dump(resps, f)

      

    driver.close()

if __name__ == '__main__':
    main()


#Eu já sabia qual api eu queria, porém eu não soube utilizar ela, então busquei por um código que pudesse puxar ela. Porém não deu certo, o código puxou todas as apis "proxytown"

#A minha idéia inicial foi fazer isso https://youtu.be/-oPuGc05Lxs?si=FgpZu7jt5RoNVuQ4. Porém o formato da api não era um https amigável como no vídeo. Era este schema, e infelizmente eu não soube trabalhar com ele:

#Obrigado pela oportunidade de realizar o teste técnico, aprendi bastante!

# {
#     "F": "161fg6yshxe.1730759920716",
#     "M": [
#         0,
#         "{\"@context\":\"https://schema.org\",\"@type\":\"Product\",\"name\":\"Smartphone Samsung Galaxy A15 6,5\\\" 128GB Azul Claro 4G 4GB RAM Câm. Tripla 50MP + Selfie 13MP 5000mAh Dual Chip\",\"image\":\"https://a-static.mlcdn.com.br/450pxx450px/smartphone-samsung-galaxy-a15-65-128gb-azul-claro-4g-4gb-ram-cam-tripla-50mp-selfie-13mp-5000mah-dual-chip/magazineluiza/237216300/febf6a6164dc08666f77a11eafecbcde.jpg\",\"brand\":\"Samsung\",\"sku\":\"237216300\",\"description\":\"O Samsung Galaxy A15 azul claro é o smartphone que vai te acompanhar em todos os momentos. Com design moderno e infinita Super AMOLED de 6,5\\\", ele é perfeito para assistir filmes, jogar e navegar nas redes sociais. Para tirar ótimas fotos, a câmera traseira é tripla de 50MP + 5MP + 2MP que garantem fotos e vídeos de alta qualidade, enquanto a câmera frontal de 13MP, é ideal para selfies e videochamadas. Para guardar diversos arquivos, ele é equipado com 128GB de armazenamento interno e os 4GB de memória RAM, garante um desempenho rápido e eficiente, mesmo em multitarefas. Para acessar a internet de onde estiver, ele tem tecnologia 4G e é Dual Chip. Além disso, tem bateria de longa duração de 5000mAh para você ficar conectado o dia todo. Produto não acompanha fone de ouvido.\",\"aggregateRating\":{\"@context\":\"https://schema.org\",\"@type\":\"AggregateRating\",\"ratingCount\":8745,\"ratingValue\":4.78},\"offers\":{\"@context\":\"https://schema.org\",\"@type\":\"Offer\",\"price\":\"809.10\",\"priceCurrency\":\"BRL\",\"availability\":\"InStock\",\"url\":\"https://www.magazineluiza.com.br/smartphone-samsung-galaxy-a15-65-128gb-azul-claro-4g-4gb-ram-cam-tripla-50mp-selfie-13mp-5000mah-dual-chip/p/237216300/te/ga15/\"},\"category\":\"Celulares e Smartphones > Galaxy A15\",\"color\":\"Azul claro\",\"itemCondition\":\"https://schema.org/NewCondition\",\"review\":[{\"@type\":\"Review\",\"author\":{\"@type\":\"Person\",\"name\":\"Cristiano\"},\"datePublished\":\"2024-11-2\",\"reviewBody\":\"Celular Top Demais Perfeito e Funcionando muito Bem Obrigado \",\"name\":null,\"reviewRating\":{\"@type\":\"Rating\",\"bestRating\":\"5\",\"ratingValue\":\"5\",\"worstRating\":\"1\"}},{\"@type\":\"Review\",\"author\":{\"@type\":\"Person\",\"name\":\"Janeide\"},\"datePublished\":\"2024-10-24\",\"reviewBody\":\"Eu amei ele ,é maravilhoso. Compre ser medo\",\"name\":null,\"reviewRating\":{\"@type\":\"Rating\",\"bestRating\":\"5\",\"ratingValue\":\"5\",\"worstRating\":\"1\"}},{\"@type\":\"Review\",\"author\":{\"@type\":\"Person\",\"name\":\"José\"},\"datePublished\":\"2024-10-23\",\"reviewBody\":\"Excelente atendimento chegou no mesmo dia bem embalado e lacrado . Recomendo muito.\\n\",\"name\":null,\"reviewRating\":{\"@type\":\"Rating\",\"bestRating\":\"5\",\"ratingValue\":\"5\",\"worstRating\":\"1\"}},{\"@type\":\"Review\",\"author\":{\"@type\":\"Person\",\"name\":\"Mirelly\"},\"datePublished\":\"2024-10-10\",\"reviewBody\":\"Gostei do produto.\\nAté agora está tudo ok \\nNão sei depois \\nComprei para a minha mãe e ela gostou\",\"name\":null,\"reviewRating\":{\"@type\":\"Rating\",\"bestRating\":\"5\",\"ratingValue\":\"4\",\"worstRating\":\"1\"}},{\"@type\":\"Review\",\"author\":{\"@type\":\"Person\",\"name\":\"Mirelly\"},\"datePublished\":\"2024-10-10\",\"reviewBody\":\"Até agora está tudo Ok.\\nNão sei depois.\\nComprei ele para o meu pai meu pai gostou \",\"name\":null,\"reviewRating\":{\"@type\":\"Rating\",\"bestRating\":\"5\",\"ratingValue\":\"5\",\"worstRating\":\"1\"}},{\"@type\":\"Review\",\"author\":{\"@type\":\"Person\",\"name\":\"Maria\"},\"datePublished\":\"2024-10-6\",\"reviewBody\":\"Celular muito bom , veio direitinho como no demonstrativo da loja ,chegou super rápido ,super indico valeu a pena amei 😍😍😍😍\",\"name\":null,\"reviewRating\":{\"@type\":\"Rating\",\"bestRating\":\"5\",\"ratingValue\":\"5\",\"worstRating\":\"1\"}},{\"@type\":\"Review\",\"author\":{\"@type\":\"Person\",\"name\":\"Alexandre\"},\"datePublished\":\"2024-10-4\",\"reviewBody\":\"Amei toda a compra, chegou no mesmo dia, foi um ótimo custo benefício e o aparelho está seguindo como o esperado até agora, espero que não tenha problemas 😅\\n...Foi minha primeira compra pelo site e app da magazine e pude acompanhar meu pedido, tirar minhas dúvidas pelo whatsapp da magalu e amei a experiência. Recomendo♡\",\"name\":null,\"reviewRating\":{\"@type\":\"Rating\",\"bestRating\":\"5\",\"ratingValue\":\"5\",\"worstRating\":\"1\"}},{\"@type\":\"Review\",\"author\":{\"@type\":\"Person\",\"name\":\"Elisangela\"},\"datePublished\":\"2024-10-4\",\"reviewBody\":\"Esse celular chegou lacrado, veio rápido, ele tem um design lindo , muito lindo a cor, eu super indico.\\nA Magalu me surpreendeu, muito obrigado equipe \\nParabéns a todos 👏👏\",\"name\":null,\"reviewRating\":{\"@type\":\"Rating\",\"bestRating\":\"5\",\"ratingValue\":\"5\",\"worstRating\":\"1\"}}]}"
#     ]
# }