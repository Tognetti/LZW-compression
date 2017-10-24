# -*- coding: utf-8 -*-
import argparse
import struct

def comprimir(input, output):
    print "Comprimindo o arquivo:", input.name
    text = input.read()

    # Constroi o dicionario inicial
    tamDicionario = 256
    dicionario = {}
    for i in xrange(tamDicionario):
        dicionario[chr(i)] = i

    compressed = []
    w = ""
    for c in text:
        wc = w + c
        if wc in dicionario:
            w = wc
        else:
            compressed.append(dicionario[w]) # adicina w no output
            dicionario[wc] = tamDicionario # adiciona a palavra nova ao dicionario
            tamDicionario += 1 # aumenta o tamanho do dicionario
            w = c
    if w: # escreve no output o que sobrou
        compressed.append(dicionario[w])

    writeBinaryFile(output, compressed)

def extrair(input, output):
    print "Descomprimindo arquivo", input.name
    texto = readBinaryFile(input.name)

    # Constroi o dicionario inicial
    tamDicionario = 256
    dicionario = {}
    for i in xrange(tamDicionario):
        dicionario[i] = chr(i)

    w = texto.pop(0)
    w = chr(w)

    uncompressed = [w]

    for k in texto:
        if k in dicionario:
            entry = dicionario[k]
        elif k == len(dicionario):
            entry = w + w[0]

        uncompressed.append(entry)
        dicionario[tamDicionario] = w + entry[0]
        tamDicionario += 1
        w = entry

    texto = ''.join(uncompressed)

    print "Escrevendo arquivo de saída"
    f = open(output, "w")
    f.write(texto)
    f.close()
    print "Escrita completa"

def writeBinaryFile(filename, array):
    print "Escrevendo arquivo binário..."
    f = open(filename, "wb")
    for a in array:
        f.write(struct.pack("!I", a))
    f.close()
    print "Arquivo binário escrito."

def readBinaryFile(filename):
    f = open(filename, "rb")
    data = []
    byte = []
    for i in range(0,4):
        readChr = f.read(1)
        byte.append('{0:08b}'.format(ord(readChr)))
    data.append(int(''.join(byte), 2))
    while readChr != "":
        byte = []
        for i in range(0,4):
            readChr = f.read(1)
            if readChr != "":
                byte.append('{0:08b}'.format(ord(readChr)))
        if len(byte) > 0:
            data.append(int(''.join(byte), 2))
    f.close()
    return data

def main():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-c", "--comprimir", help="Comprime o texto", action="store_true")
    group.add_argument("-x", "--extrair", help="Descomprime o texto", action="store_true")
    parser.add_argument("input", type=file, help="Arquivo de texto a ser comprimido")
    parser.add_argument("output", help="Nome do arquivo de saida")
    args = parser.parse_args()

    if args.comprimir:
        comprimir(args.input, args.output)
    elif args.extrair:
        extrair(args.input, args.output)
    else:
        print "Escolha uma das opções -c ou -x"

if __name__ == "__main__":
    main()
