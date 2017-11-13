# Modulação
No nosso programa a modulação de um sinal de áudio é feita da seguinte forma:
1. Dois áudios m1 e m2 são importados utilizando um pacote chamado soundfile, com isso conseguimos carregar o áudio e o samplerate.
2. Aplica-se um filtro passa-baixa nesses áudios com uma frequência de corte de 4000 Hz, para depois exibir num gráfico o Fourier dos sinais e reproduzir os novos áudios.
3. Após isso, é necessário criar uma portadora. A portadora de uma modulação é o sinal que irá “carregar” a mensagem, a combinação da portadora mais a mensagem gera o sinal modulado. A primeira portadora possui uma frequência de 5000 Hz enquanto a segunda de 15000 Hz.
4. As portadoras são criadas a partir da função `np.sin(2*np.pi*self.fc*t)` com `self.fc` sendo as frequências das portadoras e `t` sendo `np.linspace(0, len(m_filtrado)/44100,len(m_filtrado))`.
5. Então multiplicamos o áudio filtrado pela portadora, gerando dois áudios modulados. Reproduzimos os dois áudios para verificar e depois os somamos para realizar a transmissão.

# Demodulação
No nosso programa a demodulação de um sinal de áudio é feita da seguinte forma:
1. Primeiro gravamos o áudio modulado e exibimos o Fourier do sinal recebido.
2. Após isso, reconstruímos as portadoras originais e multiplicamos pelo áudio total, recuperando um dos áudios originais de cada vez.
3. Aplicamos um filtro passa-baixas com a mesma frequência de corte de 4000 Hz e reproduzimos os sinais para verificar se houve perda de informação.
4. Por fim, salvamos os sinais recuperados.

# Portadoras
Utilizamos frequências de 5000 Hz e 15000 Hz para construir as portadoras, mantendo a largura de banda para que elas não se 'atropelem'.

# Bandas ocupadas
Como utilizamos uma frequência de corte de 4000 Hz, a banda ocupada é de 8000Hz.

# Transmissor vs Receptor
 Este é o sinal transmitido:

![Transmitido](https://i.imgur.com/RmISlcb.jpg)

 Este é o sinal recebido:

![Recebido](https://i.imgur.com/tZ5MZTI.jpg)

Podemos perceber que o gráfico do transmitido contém as duas mensagens num mesmo sinal modulado, enquanto que o recebido está exibindo os áudios demodulados um em cima do outro (dois plots diferentes).

# Os sinais (mensagens) a serem transmitidas no tempo
![Transmitido](https://github.com/filipefborba/dtmf_raphorba/blob/master/mod-demod-am/raphorbatempo.png)
![Transmitido](https://github.com/filipefborba/dtmf_raphorba/blob/master/mod-demod-am/trabsontempo.png)

# O Fourier dos sinais (frequência)
![Transmitido](https://github.com/filipefborba/dtmf_raphorba/blob/master/mod-demod-am/raphorba_fourier.png)
![Transmitido](https://github.com/filipefborba/dtmf_raphorba/blob/master/mod-demod-am/trabson_fourier.png)

# As portadoras no tempo
![Transmitido](https://github.com/filipefborba/dtmf_raphorba/blob/master/mod-demod-am/port1time.png)
![Transmitido](https://github.com/filipefborba/dtmf_raphorba/blob/master/mod-demod-am/port2time.png)

# As mensagens moduladas e demoduladas no tempo	
![Transmitido](https://github.com/filipefborba/dtmf_raphorba/blob/master/mod-demod-am/mensagem1modtempo.png)
![Transmitido](https://github.com/filipefborba/dtmf_raphorba/blob/master/mod-demod-am/mensagem2modetempo.png)

![Transmitido](https://github.com/filipefborba/dtmf_raphorba/blob/master/mod-demod-am/mensagem1dmodtempo.png)
![Transmitido](https://github.com/filipefborba/dtmf_raphorba/blob/master/mod-demod-am/mensagem2dmodtempo.png)

