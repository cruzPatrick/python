frase = 'Da Like!'
print(frase)
print(frase[4])
print(frase[3:8])
print(frase[1:])
print(frase[:4])
print(frase[0::2])

print(frase.count('a'))
print(frase.count('A'))
print(frase.upper().count('A')) #transformou tudo em maiúsculo e viu quantos A tinham
print(len(frase))

print(frase.replace('Da', 'Deixa o'))

frase.replace('Da', 'Deixa o')
print(frase)

frase = frase.replace('Da', 'Deixa o')
print(frase)
print('Like' in frase)
print(frase.find('Like'))
dividido = frase.split()
print(dividido[0])
print(dividido[2][2])

'''print("""Conheça o Hangul:
Certifique-se de que você está familiarizado com o alfabeto coreano (Hangul) e suas combinações de consoantes e vogais. Isso ajudará você a ler mais rapidamente e com mais fluidez.
Pratique regularmente:
A prática constante é fundamental para aumentar a velocidade da leitura. Leia textos em coreano regularmente, começando com material mais fácil e progredindo para textos mais desafiadores à medida que você se sentir mais confortável.
Leia em voz alta:
Ler em voz alta pode ajudar a aumentar sua velocidade de leitura, pois força você a pronunciar as palavras mais rapidamente. Isso também ajuda a melhorar sua compreensão auditiva e pronúncia.
Use recursos de áudio:
Combine a leitura com recursos de áudio, como podcasts, audiolivros ou vídeos em coreano. Isso ajudará você a se acostumar com a velocidade natural da fala em coreano e a melhorar sua compreensão auditiva.
Pratique técnicas de leitura rápida:
Experimente técnicas de leitura rápida, como leitura em blocos, em que você move os olhos em grupos de palavras em vez de palavra por palavra. Isso pode ajudar a reduzir a subvocalização e aumentar sua velocidade de leitura.
Expanda seu vocabulário:
Quanto mais vocabulário você conhece, mais rápido você será capaz de ler. Tente aprender novas palavras regularmente e pratique a leitura de diferentes tipos de texto para expor-se a uma variedade de vocabulário.
Estabeleça metas de leitura:
Defina metas específicas para a quantidade de texto que você deseja ler por dia ou por semana e trabalhe para alcançá-las. Isso pode ajudar a manter sua motivação e a impulsionar seu progresso na leitura.
Use aplicativos e recursos online:
Existem muitos aplicativos e recursos online disponíveis para praticar a leitura em coreano, como aplicativos de aprendizado de idiomas, sites de notícias em coreano e fóruns online. Experimente diferentes recursos e encontre aqueles que funcionam melhor para você.""")'''