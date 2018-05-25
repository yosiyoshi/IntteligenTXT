# -*- coding: utf-8 -*-
"""
Created on Fri May 18 17:39:44 2018

@author: YosiYoshi
"""
from __future__ import unicode_literals

import tkinter.filedialog as tkfd
import sys
sys.path.append("../")

import pythainlp as ptn

import cutkum

import jieba
import jieba.posseg
import jieba.analyse

from pymecab.pymecab import PyMecab

import deepseg

from pyvi import ViTokenizer, ViPosTagger

import tltk.nlp as tl

import tkinter as tk

class Frame(tk.Frame):
    root = tk.Tk()
    m = tk.StringVar()

    def main():
        root = Frame.root
        m = Frame.m
        root.title('Editor')
        root.geometry("800x25")
        
        menub1 = tk.Menu(root, tearoff=0)
        root.configure(menu = menub1)
        menuf1 = tk.Menu(menub1, tearoff=0)
        menuf0 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"File", menu=menuf0,  underline=5)
        menuf0.add_command(label=u"Save", command=Frame.save, underline=5, accelerator = 'Ctrl-S')

        menub1.add_cascade(label=u"NLP(ZH)", menu=menuf1,  underline=5)
        menuf1.add_command(label=u"Tokenize", command=Frame.segzh, underline=5, accelerator = 'Ctrl-T')
#        menuf1.add_command(label=u"Deepseg", command=Frame.dsegzh, underline=5, accelerator = 'Ctrl-D')
        menuf1.add_command(label=u"Keywords", command=Frame.kwzh, underline=5, accelerator = 'Ctrl-K')
        menuf1.add_command(label=u"POS", command=Frame.poszh, underline=5, accelerator = 'Ctrl-P')
    
        menuf2 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(TH)", menu=menuf2,  underline=5)
        menuf2.add_command(label=u"Tokenize", command=Frame.segth, underline=5, accelerator = 'Ctrl-T')
        menuf2.add_command(label=u"DeepCut", command=Frame.dsegth, underline=5, accelerator = 'Ctrl-D')
#        menuf2.add_command(label=u"Cutkum", command=Frame.ckth, underline=5, accelerator = 'Ctrl-C')
        menuf2.add_command(label=u"Romanize", command=Frame.romth, underline=5, accelerator = 'Ctrl-R')
        menuf2.add_command(label=u"Keywords", command=Frame.kwth, underline=5, accelerator = 'Ctrl-K')
        menuf2.add_command(label=u"POS", command=Frame.posth, underline=5, accelerator = 'Ctrl-P')
        menuf2.add_command(label=u"Summary", command=Frame.sumth, underline=5, accelerator = 'Ctrl-S')
        menuf2.add_command(label=u"sentiMent", command=Frame.senth, underline=5, accelerator = 'Ctrl-M')
        menuf2.add_command(label=u"speLL", command=Frame.splth, underline=5, accelerator = 'Ctrl-L')
        
        menuf3 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(VT)", menu=menuf3,  underline=5)
        menuf3.add_command(label=u"Tokenize", command=Frame.segvt, underline=5, accelerator = 'Ctrl-T')
        menuf3.add_command(label=u"POS", command=Frame.posvt, underline=5, accelerator = 'Ctrl-P')

#        menuf4 = tk.Menu(menub1, tearoff=0)
#        menub1.add_cascade(label=u"NLP(JP)", menu=menuf4,  underline=5)
#        menuf4.add_command(label=u"Tokenize", command=Frame.mcjp, underline=5, accelerator = 'Ctrl-T')
        
        entry = tk.Entry(root,font=("",14),justify="left", textvariable=m) #entry textbox
        entry.pack(fill="x")
        root.mainloop()

    def save():
        fn = tkfd.askopenfilename()
        m = Frame.m
        f = open(fn, 'w')
        f.write(m)
        f.close()
 
    def segzh():
        m = Frame.m
        txt = m.get()
        seg = "/ ".join(jieba.cut(txt, cut_all=False))
        print(seg)
        root2 = tk.Tk()
        root2.title('Result(SegmentZH)')
        label2 = tk.Label(root2,text=seg,font=16)
        label2.pack(fill="x")
        root2.mainloop()
        
    def kwzh():
        m = Frame.m
        txt = m.get()
        root6 = tk.Tk()
        root6.title('Result(KeywordsZH)')
        for x, w in jieba.analyse.extract_tags(txt, withWeight=True):
            print('%s %s' % (x, w))
            label6 = tk.Label(root6,text='%s %s' % (x, w),font=16)
            label6.pack(fill="x")
        root6.mainloop()
        
    def poszh():
        m = Frame.m
        txt = m.get()
        words = jieba.posseg.cut(txt)
        root7 = tk.Tk()
        root7.title('Result(POS-ZH)')
        for w in words:
            print('%s %s' % (w.word, w.flag))
            label7 = tk.Label(root7,text='%s %s' % (w.word, w.flag),font=16)
            label7.pack(fill="x")
        root7.mainloop()

    def segth():
        m = Frame.m
        txt = m.get()
        seg = tl.segment(txt)
        print(seg)
        root3 = tk.Tk()
        root3.title('Result(SegmentTH)')
        label3 = tk.Label(root3,text=seg,font=16)
        label3.pack(fill="x")
        root3.mainloop()

    def romth():
        m = Frame.m
        txt = m.get()
        seg = ptn.romanization(txt,engine='royin')
        print(seg)
        root5 = tk.Tk()
        root5.title('Result(RomanTH)')
        label5 = tk.Label(root5,text=seg,font=16)
        label5.pack(fill="x")
        root5.mainloop()
       
    def posth():
        m = Frame.m
        txt = m.get()
        seg = tl.pos_tag(txt)
        print(seg)
        root8 = tk.Tk()
        root8.title('Result(POS-TH)')
        label8 = tk.Label(root8,text=seg,font=16)
        label8.pack(fill="x")
        root8.mainloop()
    
    def segvt():
        m = Frame.m
        txt = m.get()
        seg = ViTokenizer.tokenize(txt)
        print(seg)
        root9 = tk.Tk()
        root9.title('Result(KeywordsVT)')
        label9 = tk.Label(root9,text=seg,font=16)
        label9.pack(fill="x")
        root9.mainloop()

    def posvt():
        m = Frame.m
        txt = m.get()
        seg = ViPosTagger.postagging(ViTokenizer.tokenize(txt))
        print(seg)
        root10 = tk.Tk()
        label0 = tk.Label(root10,text=seg,font=16)
        label0.pack(fill="x")
        root10.title('Result(POS-VT)')
        root10.mainloop()
        
    def sumth():
        m = Frame.m
        txt = m.get()
        seg = ptn.summarize.summarize_text(txt,n=1,engine='frequency')
        print(seg)
        root11 = tk.Tk()
        label1 = tk.Label(root11,text=seg,font=16)
        label1.pack(fill="x")
        root11.title('Result(SummaryTH)')
        root11.mainloop()

    def dsegth():
        m = Frame.m
        txt = m.get()
        seg = ptn.word_tokenize(txt,engine='deepcut')
        print(seg)
        root12 = tk.Tk()
        root12.title('Result(DeepCutTH)')
        label12 = tk.Label(root12,text=seg,font=16)
        label12.pack(fill="x")
        root12.mainloop()
        
#    def ckth():
#        m = Frame.m
#        txt = m.get()
#        seg = cutkum.tokenize(txt)
#        print(seg)
#        root13 = tk.Tk()
#        root13.title('Result(CutkumTH)')
#        label13 = tk.Label(root13,text=seg,font=16)
#        label13.pack(fill="x")
#        root13.mainloop()

#    def dsegzh():
#        m = Frame.m
#        txt = m.get()
#        seg = deepseg.cut(txt)
#        print(" ".join(seg))
#        root14 = tk.Tk()
#        root14.title('Result(DeepSegZH)')
#        label14 = tk.Label(root14,text=seg,font=16)
#        label14.pack(fill="x")
#        root14.mainloop()
        
#    def mcjp():
#        m = Frame.m
#        txt = m.get()
#        mecab = PyMecab()
#        root15 = tk.Tk()
#        root15.title('Result(MecabJP)')
#        for token in mecab.tokenize(txt):
#            print(token.surface, token.pos1)
#            label15 = tk.Label(root15,text=token.surface+" "+token.pos1,font=16)
#            label15.pack(fill="x")    
#        root15.mainloop()

    def kwth():
        m = Frame.m
        txt = m.get()
        seg = ptn.word_tokenize(txt,engine='deepcut')
        print(seg)
        kw = ptn.find_keyword(seg, lentext=3)
        print(kw)
        root16 = tk.Tk()
        root16.title('Result(KeywordTH)')
        label16 = tk.Label(root16,text=kw)
        label16.pack(fill="x")
        root16.mainloop()
        
    def senth():
        m = Frame.m
        txt = m.get()
        seg = ptn.sentiment(txt)
        print(seg)
        root17 = tk.Tk()
        root17.title('Result(SentimentTH)')
        label17 = tk.Label(root17,text=seg)
        label17.pack(fill="x")
        root17.mainloop()

    def splth():
        m = Frame.m
        txt = m.get()
        seg = ptn.spell(txt,engine='pn')
        print(seg)
        root18 = tk.Tk()
        root18.title('Result(SentimentTH)')
        label18 = tk.Label(root18,text=seg)
        label18.pack(fill="x")
        root18.mainloop()
        
if __name__ == '__main__':
    f = Frame()
    Frame.main()
        menuf1.add_command(label=u"POS", command=Frame.poszh, underline=5, accelerator = 'Ctrl-P')
    
        menuf2 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(TH)", menu=menuf2,  underline=5)
        menuf2.add_command(label=u"Tokenize", command=Frame.segth, underline=5, accelerator = 'Ctrl-T')
        menuf2.add_command(label=u"DeepCut", command=Frame.dsegth, underline=5, accelerator = 'Ctrl-D')
#        menuf2.add_command(label=u"Cutkum", command=Frame.ckth, underline=5, accelerator = 'Ctrl-C')
        menuf2.add_command(label=u"Romanize", command=Frame.romth, underline=5, accelerator = 'Ctrl-R')
        menuf2.add_command(label=u"POS", command=Frame.posth, underline=5, accelerator = 'Ctrl-P')
        menuf2.add_command(label=u"Summary", command=Frame.sumth, underline=5, accelerator = 'Ctrl-S')
        
        menuf3 = tk.Menu(menub1, tearoff=0)
        menub1.add_cascade(label=u"NLP(VT)", menu=menuf3,  underline=5)
        menuf3.add_command(label=u"Tokenize", command=Frame.segvt, underline=5, accelerator = 'Ctrl-T')
        menuf3.add_command(label=u"POS", command=Frame.posvt, underline=5, accelerator = 'Ctrl-P')

        entry = tk.Entry(root,font=("",14),justify="left", textvariable=m) #entry textbox
        entry.pack(fill="x")
        root.mainloop()

    def save():
        fn = tkfd.askopenfilename()
        m = Frame.m
        f = open(fn, 'w')
        f.write(m)
        f.close()
 
    def segzh():
        m = Frame.m
        txt = m.get()
        seg = "/ ".join(jieba.cut(txt, cut_all=False))
        print(seg)
        root2 = tk.Tk()
        root2.title('Result(SegmentZH)')
        label2 = tk.Label(root2,text=seg,font=16)
        label2.pack(fill="x")
        root2.mainloop()
        
    def kwzh():
        m = Frame.m
        txt = m.get()
        root6 = tk.Tk()
        root6.title('Result(KeywordsZH)')
        for x, w in jieba.analyse.extract_tags(txt, withWeight=True):
            print('%s %s' % (x, w))
            label6 = tk.Label(root6,text='%s %s' % (x, w),font=16)
            label6.pack(fill="x")
        root6.mainloop()
        
    def poszh():
        m = Frame.m
        txt = m.get()
        words = jieba.posseg.cut(txt)
        root7 = tk.Tk()
        root7.title('Result(POS-ZH)')
        for w in words:
            print('%s %s' % (w.word, w.flag))
            label7 = tk.Label(root7,text='%s %s' % (w.word, w.flag),font=16)
            label7.pack(fill="x")
        root7.mainloop()

    def segth():
        m = Frame.m
        txt = m.get()
        seg = tl.segment(txt)
        print(seg)
        root3 = tk.Tk()
        root3.title('Result(SegmentTH)')
        label3 = tk.Label(root3,text=seg,font=16)
        label3.pack(fill="x")
        root3.mainloop()

    def romth():
        m = Frame.m
        txt = m.get()
        seg = ptn.romanization(txt,engine='royin')
        print(seg)
        root5 = tk.Tk()
        root5.title('Result(RomanTH)')
        label5 = tk.Label(root5,text=seg,font=16)
        label5.pack(fill="x")
        root5.mainloop()
       
    def posth():
        m = Frame.m
        txt = m.get()
        seg = tl.pos_tag(txt)
        print(seg)
        root8 = tk.Tk()
        root8.title('Result(POS-TH)')
        label8 = tk.Label(root8,text=seg,font=16)
        label8.pack(fill="x")
        root8.mainloop()
    
    def segvt():
        m = Frame.m
        txt = m.get()
        seg = ViTokenizer.tokenize(txt)
        print(seg)
        root9 = tk.Tk()
        root9.title('Result(KeywordsVT)')
        label9 = tk.Label(root9,text=seg,font=16)
        label9.pack(fill="x")
        root9.mainloop()

    def posvt():
        m = Frame.m
        txt = m.get()
        seg = ViPosTagger.postagging(ViTokenizer.tokenize(txt))
        print(seg)
        root10 = tk.Tk()
        label0 = tk.Label(root10,text=seg,font=16)
        label0.pack(fill="x")
        root10.title('Result(POS-VT)')
        root10.mainloop()
        
    def sumth():
        m = Frame.m
        txt = m.get()
        seg = ptn.summarize.summarize_text(txt,n=1,engine='frequency')
        print(seg)
        root11 = tk.Tk()
        label1 = tk.Label(root11,text=seg,font=16)
        label1.pack(fill="x")
        root11.title('Result(SummaryTH)')
        root11.mainloop()

    def dsegth():
        m = Frame.m
        txt = m.get()
        seg = ptn.word_tokenize(txt,engine='deepcut')
        print(seg)
        root12 = tk.Tk()
        root12.title('Result(DeepCutTH)')
        label12 = tk.Label(root12,text=seg,font=16)
        label12.pack(fill="x")
        root12.mainloop()
        
#    def ckth():
#        m = Frame.m
#        txt = m.get()
#        seg = cutkum.tokenize(txt)
#        print(seg)
#        root13 = tk.Tk()
#        root13.title('Result(CutkumTH)')
#        label13 = tk.Label(root13,text=seg,font=16)
#        label13.pack(fill="x")
#        root13.mainloop()

#    def dsegzh():
#        m = Frame.m
#        txt = m.get()
#        seg = deepseg.cut(txt)
#        print(" ".join(seg))
#        root14 = tk.Tk()
#        root14.title('Result(DeepSegZH)')
#        label14 = tk.Label(root14,text=seg,font=16)
#        label14.pack(fill="x")
#        root14.mainloop()

if __name__ == '__main__':
    f = Frame()
    Frame.main()

        entry = tk.Entry(root,font=("",14),justify="left", textvariable=m) #entry textbox
        entry.pack(fill="x")
        root.mainloop()

    def segzh():
        m = Frame.m
        txt = m.get()
        seg = "/ ".join(jieba.cut(txt, cut_all=False))
        print(seg)
        root2 = tk.Tk()
        root2.title('Result(SegmentZH)')
        label2 = tk.Label(root2,text=seg,font=16)
        label2.pack(fill="x")
        root2.mainloop()
        
    def kwzh():
        m = Frame.m
        txt = m.get()
        root6 = tk.Tk()
        root6.title('Result(KeywordsZH)')
        for x, w in jieba.analyse.extract_tags(txt, withWeight=True):
            print('%s %s' % (x, w))
            label6 = tk.Label(root6,text='%s %s' % (x, w),font=16)
            label6.pack(fill="x")
        root6.mainloop()
        
    def poszh():
        m = Frame.m
        txt = m.get()
        words = jieba.posseg.cut(txt)
        root7 = tk.Tk()
        root7.title('Result(POS-ZH)')
        for w in words:
            print('%s %s' % (w.word, w.flag))
            label7 = tk.Label(root7,text='%s %s' % (w.word, w.flag),font=16)
            label7.pack(fill="x")
        root7.mainloop()

    def segth():
        m = Frame.m
        txt = m.get()
        seg = tl.segment(txt)
        print(seg)
        root3 = tk.Tk()
        root3.title('Result(SegmentTH)')
        label3 = tk.Label(root3,text=seg,font=16)
        label3.pack(fill="x")
        root3.mainloop()
        
#    def ipath():
#        m = Frame.m
#        txt = m.get()
#        seg = tl.th2ipa(txt)
#        print(seg)
#        root4 = tk.Tk()
#        root4.title('Result(IPA-TH)')
#        label4 = tk.Label(root4,text=seg,font=16)
#        label4.pack(fill="x")
#        root4.mainloop()
#
#    def romth():
#        m = Frame.m
#        txt = m.get()
#        seg = tl.th2roman(txt)
#        print(seg)
#        root5 = tk.Tk()
#        root5.title('Result(RomanTH)')
#        label5 = tk.Label(root5,text=seg,font=16)
#        label5.pack(fill="x")
#        root5.mainloop()
#       
    def posth():
        m = Frame.m
        txt = m.get()
        seg = tl.pos_tag(txt)
        print(seg)
        root8 = tk.Tk()
        root8.title('Result(POS-TH)')
        label8 = tk.Label(root8,text=seg,font=16)
        label8.pack(fill="x")
        root8.mainloop()
    
    def segvt():
        m = Frame.m
        txt = m.get()
        seg = ViTokenizer.tokenize(txt)
        print(seg)
        root9 = tk.Tk()
        root9.title('Result(KeywordsVT)')
        label9 = tk.Label(root9,text=seg,font=16)
        label9.pack(fill="x")
        root9.mainloop()

    def posvt():
        m = Frame.m
        txt = m.get()
        seg = ViPosTagger.postagging(ViTokenizer.tokenize(txt))
        print(seg)
        root10 = tk.Tk()
        label0 = tk.Label(root10,text=seg,font=16)
        label0.pack(fill="x")
        root10.title('Result(POS-VT)')
        root10.mainloop()

        
if __name__ == '__main__':
    f = Frame()
    Frame.main()
        seg = "/ ".join(jieba.cut(txt, cut_all=False))
        print(seg)
        root2 = tk.Tk()
        root2.title('Result(SegmentZH)')
        label2 = tk.Label(root2,text=seg,font=16)
        label2.pack(fill="x")
        root2.mainloop()
        
    def kwzh():
        m = Frame.m
        txt = m.get()
        root6 = tk.Tk()
        root6.title('Result(KeywordsZH)')
        for x, w in jieba.analyse.extract_tags(txt, withWeight=True):
            print('%s %s' % (x, w))
            label6 = tk.Label(root6,text='%s %s' % (x, w),font=16)
            label6.pack(fill="x")
        root6.mainloop()
        
#    def poszh():
#        m = Frame.m
#        txt = m.get()
#        words = jieba.posseg.cut(txt)
#        root7 = tk.Tk()
#        root7.title('Result(POS-ZH)')
#        for word, flag in words:
#            print('%s %s' % (word, flag))
#            label7 = tk.Label(root7,text='%s %s' % (word, flag),font=16)
#            label7.pack(fill="x")
#        root7.mainloop()

    def segth():
        m = Frame.m
        txt = m.get()
        seg = tl.segment(txt)
        print(seg)
        root3 = tk.Tk()
        root3.title('Result(SegmentTH)')
        label3 = tk.Label(root3,text=seg,font=16)
        label3.pack(fill="x")
        root3.mainloop()
        
#    def ipath():
#        m = Frame.m
#        txt = m.get()
#        seg = tl.th2ipa(txt)
#        print(seg)
#        root4 = tk.Tk()
#        root4.title('Result(IPA-TH)')
#        label4 = tk.Label(root4,text=seg,font=16)
#        label4.pack(fill="x")
#        root4.mainloop()
#
#    def romth():
#        m = Frame.m
#        txt = m.get()
#        seg = tl.th2roman(txt)
#        print(seg)
#        root5 = tk.Tk()
#        root5.title('Result(RomanTH)')
#        label5 = tk.Label(root5,text=seg,font=16)
#        label5.pack(fill="x")
#        root5.mainloop()
#       
    def posth():
        m = Frame.m
        txt = m.get()
        seg = tl.pos_tag(txt)
        print(seg)
        root8 = tk.Tk()
        root8.title('Result(POS-TH)')
        label8 = tk.Label(root8,text=seg,font=16)
        label8.pack(fill="x")
        root8.mainloop()
        
if __name__ == '__main__':
    f = Frame()
    Frame.main()