from datetime import datetime
import instaloader

# Carregar a Lib e faz Login com a conta desejada #

L = instaloader.Instaloader()
L.login('USER do perfil', 'SENHA')

# Carrega todos os posts do perfil escolhido #
posts = instaloader.Profile.from_username(L.context, 'PERFIL ESCOLHIDO').get_posts()

# Período que deseja baixar os Posts #
SINCE = datetime(2021,1,16)
UNTIL = datetime(2022,1,18)

# Percorre os posts e baíxa apenas os que estão dentro do período desejado #
for post in posts:
    if (post.date >= SINCE) and (post.date <= UNTIL):
        print(post.date)
        L.download_post(post, 'insta-posts-downloads')
