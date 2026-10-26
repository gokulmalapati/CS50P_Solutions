import sys
import emoji

def main():
    print( "Output :" + emojize(input("Input:")))

def emojize(text):
    return emoji.emojize(text , language = 'alias')

main()
