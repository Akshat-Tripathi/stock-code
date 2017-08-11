
# coding: utf-8

# In[1]:

from pandas import DataFrame, read_csv
import pandas as pd
import time


# In[2]:

def download(share):
        url_template = "http://www.google.com/finance/historical?output=csv&q={stock}"
        url = url_template.format(stock=share)
        df = pd.read_csv(url)
        df.to_csv('a' + share + '.csv',index=True,header=True)
        print(share)


# In[3]:

Location = r'C:\Users\aksha\Documents\weight.csv'
df = pd.read_csv(Location)
w1 = float(df['weight'][0])
w2 = float(df['weight'][1])
w3 = float(df['weight'][2])
w4 = float(df['weight'][3])
w5 = float(df['weight'][4])
w6 = float(df['weight'][5])
w7 = float(df['weight'][6])
w8 = float(df['weight'][7])
w9 = float(df['weight'][8])
w10 = float(df['weight'][9])
w11 = float(df['weight'][10])
w12 = float(df['weight'][11])
w13 = float(df['weight'][12])
w14 = float(df['weight'][13])
w15 = float(df['weight'][14])
w16 = float(df['weight'][15])
w17 = float(df['weight'][16])
w18 = float(df['weight'][17])
epoch = float(df['weight'][18])
predicted = []
actual = []
vol = 8
s = 0
delta = 0
lr = 0.00001
List = []
print('Download')
ans = input().lower()
if(ans == "yes"):
    FTSE =[ 'III.L' , 'ADM.L', 'AAL.L', 'ANTO.L', 'AHT.L', 'ABF.L', 'AZN.L', 'AV.L', 'BAB.L', 'BA.L', 'BARC.L', 'BDEV.L', 'BLT.L', 'BP.L', 'BATS.L', 'BLND.L', 'BT.L', 'BNZL.L', 'BRBY.L', 'CPI.L', 'CCL.L', 'CNA.L', 'CCH.L', 'CPG.L', 'CRH.L', 'DCC.L', 'DGE.L', 'DLG.L', 'DC.L', 'EZJ.L', 'EXPN.L', 'FRES.L', 'GKN.L', 'GSK.L', 'GLEN.L', 'HMSO.L', 'HL.L', 'HIK.L', 'HSBA.L', 'IMB.L', 'INF.L', 'IHG.L', 'IAG.L', 'ITRK.L', 'INTU.L', 'ITV.L', 'SBRY.L', 'JMAT.L', 'KGF.L', 'LAND.L', 'LGEN.L', 'LLOY.L', 'LSE.L', 'MKS.L', 'MDC.L', 'MERL.L', 'MCRO.L', 'MNDI.L', 'NG.L', 'NXT.L', 'OML.L', 'PPB.L', 'PSON.L', 'PSN.L', 'POLY.L', 'PFG.L', 'PRU.L', 'RRS.L', 'RB.L', 'REL.L', 'RIO.L', 'RR.L', 'RBS.L', 'RDSA.L', 'RMG.L', 'RSA.L', 'SGE.L', 'SDR.L', 'SVT.L', 'SHP.L', 'SKY.L', 'SN.L', 'SMIN.L', 'SSE.L', 'STJ.L', 'STAN.L', 'SL.L', 'TW.L', 'TSCO.L', 'TPK.L', 'TUI.L', 'ULVR.L', 'UU.L', 'VOD.L', 'WTB.L', 'MRW.L', 'FERG.L', 'WPG.L', 'WPP.L', 'ABC.L', 'AN.L', 'ASHM.L', 'BBA.L', 'BKG.L', 'BYG.L', 'BVIC.L', 'CHG.L', 'CCC.L', 'DMGT.L', 'DEB.L', 'DLN.L', 'DSG.L', 'DOM.L', 'DRX.L', 'ECM.L', 'ELM.L', 'EIG.L', 'EVR.L', 'FXPO.L', 'FGP.L', 'GNS.L', 'HFD.L', 'HWDN.L', 'HCM.L', 'IAP.L', 'INCH.L', 'JDW.L', 'JD.L', 'KBT.L', 'KAZ.L', 'LAM.L', 'MLD.L', 'MONY.L', 'MPE.L', 'NEX.L', 'OCDO.L', 'PNN.L', 'QQ.L', 'RNK.L', 'RTO.L', 'RMV.L', 'SVS.L', 'SHB.L', 'SHI.L', 'TALK.L', 'VEC.L', 'VSVS.L', 'YOU.L', 'ZYT.L']
    for i in range(149):
        share = FTSE[i]
        download(share)
loop = 'yes'
print('Do you want to train or test this artificial intelligence?')
ans = input()


# In[4]:

def train(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, s, epoch, vol, delta):
    Location = r'C:\Users\aksha\Documents\weight.csv'
    df = pd.read_csv(Location)
    w1 = float(df['weight'][0])
    w2 = float(df['weight'][1])
    w3 = float(df['weight'][2])
    w4 = float(df['weight'][3])
    w5 = float(df['weight'][4])
    w6 = float(df['weight'][5])
    w7 = float(df['weight'][6])
    w8 = float(df['weight'][7])
    w9 = float(df['weight'][8])
    w10 = float(df['weight'][9])
    w11 = float(df['weight'][10])
    w12 = float(df['weight'][11])
    w13 = float(df['weight'][12])
    w14 = float(df['weight'][13])
    w15 = float(df['weight'][14])
    w16 = float(df['weight'][15])
    w17 = float(df['weight'][16])
    w18 = float(df['weight'][17])
    epoch = float(df['weight'][18])
    s = 0
    vol = 8
    delta = 0
    lr = 0.00001
    epoch = epoch + 1
    save = []
    FTSE =['III.L' , 'ADM.L', 'AAL.L', 'ANTO.L', 'AHT.L', 'ABF.L', 'AZN.L', 'AV.L', 'BAB.L', 'BA.L', 'BARC.L', 'BDEV.L', 'BLT.L', 'BP.L', 'BATS.L', 'BLND.L', 'BT.L', 'BNZL.L', 'BRBY.L', 'CPI.L', 'CCL.L', 'CNA.L', 'CCH.L', 'CPG.L', 'CRH.L', 'DCC.L', 'DGE.L', 'DLG.L', 'DC.L', 'EZJ.L', 'EXPN.L', 'FRES.L', 'GKN.L', 'GSK.L', 'GLEN.L', 'HMSO.L', 'HL.L', 'HIK.L', 'HSBA.L', 'IMB.L', 'INF.L', 'IHG.L', 'IAG.L', 'ITRK.L', 'INTU.L', 'ITV.L', 'SBRY.L', 'JMAT.L', 'KGF.L', 'LAND.L', 'LGEN.L', 'LLOY.L', 'LSE.L', 'MKS.L', 'MDC.L', 'MERL.L', 'MCRO.L', 'MNDI.L', 'NG.L', 'NXT.L', 'OML.L', 'PPB.L', 'PSON.L', 'PSN.L', 'POLY.L', 'PFG.L', 'PRU.L', 'RRS.L', 'RB.L', 'REL.L', 'RIO.L', 'RR.L', 'RBS.L', 'RDSA.L', 'RMG.L', 'RSA.L', 'SGE.L', 'SDR.L', 'SVT.L', 'SHP.L', 'SKY.L', 'SN.L', 'SMIN.L', 'SSE.L', 'STJ.L', 'STAN.L', 'SL.L', 'TW.L', 'TSCO.L', 'TPK.L', 'TUI.L', 'ULVR.L', 'UU.L', 'VOD.L', 'WTB.L', 'MRW.L', 'FERG.L', 'WPG.L', 'WPP.L', 'ABC.L', 'AN.L', 'ASHM.L', 'BBA.L', 'BKG.L', 'BYG.L', 'BVIC.L', 'CHG.L', 'CCC.L', 'DMGT.L', 'DEB.L', 'DLN.L', 'DSG.L', 'DOM.L', 'DRX.L', 'ECM.L', 'ELM.L', 'EIG.L', 'EVR.L', 'FXPO.L', 'FGP.L', 'GNS.L', 'HFD.L', 'HWDN.L', 'HCM.L', 'IAP.L', 'INCH.L', 'JDW.L', 'JD.L', 'KBT.L', 'KAZ.L', 'LAM.L', 'MLD.L', 'MONY.L', 'MPE.L', 'NEX.L', 'OCDO.L', 'PNN.L', 'QQ.L', 'RNK.L', 'RTO.L', 'RMV.L', 'SVS.L', 'SHB.L', 'SHI.L', 'TALK.L', 'VEC.L', 'VSVS.L', 'YOU.L', 'ZYT.L']
    for i in range(149):
        share = FTSE[i]
        Location = r'C:\Users\aksha\Documents\Akshat\AI - Stocks\a'+ share + '.csv'
        df = pd.read_csv(Location)
        for i in range(3, len(df)-5):
            breakk = False
            PClose = df['Close'][i-2:i-1]
            NClose = df['Close'][i:i+1]
            NNClose = df['Close'][i+1:i+2]
            if (df['Open'][i-1:i]).dtype == "float64":
                Open = float(df['Open'][i-1:i])
            else:
                breakk = True
            
            if (df['High'][i-1:i]).dtype == "float64":
                High = float(df['High'][i-1:i])
            else:
                breakk = True
            
            if (df['Low'][i-1:i]).dtype == "float64":
                Low = float(df['Low'][i-1:i])
            else:
                breakk = True
            
            if (NClose).dtype == "float64":
                nClose = float(NClose)
            else:
                breakk = True

            if (PClose).dtype == "float64":
                pClose = float(PClose)
            else:
                breakk = True
            
            if (NNClose).dtype == "float64":
                nnClose = float(NNClose)
            else:
                breakk = True
                
            if breakk == True:
                break
            
            N1 = (Open*w1 + High*w2 + Low*w3 + pClose*w4)/4
            if N1>nClose :
                w1 = w1-lr
            if N1<nClose :
                w1 = w1+lr
            if N1>nClose :
                w2 = w2-lr
            if N1<nClose :
                w2 = w2+lr
            if N1>nClose :
                w3 = w3-lr
            if N1<nClose :
                w3 = w3+lr
            if N1>nClose :
                w4 = w4-lr
            if N1<nClose :
                w4 = w4+lr
                    
            if abs(nClose-(Open*w1))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w1 = w1-lr
                if pClose<nClose:
                    w1 = w1+lr
            if abs(nClose-(High*w2))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w2 = w2-lr
                if pClose<nClose:
                    w2 = w2+lr
            if abs(nClose-(Low*w3))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w3 = w3-lr
                if pClose<nClose:
                    w3 = w3+lr
            if abs(nClose-(pClose*w4))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w4 = w4-lr
                if pClose<nClose:
                    w4 = w4+lr
                        
            if abs(nClose-(Open*w1))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w1 = w1-lr
                if nnClose<nClose:
                    w1 = w1+lr
            if abs(nClose-(High*w2))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w2 = w2-lr
                if nnClose<nClose:
                    w2 = w2+lr
            if abs(nClose-(Low*w3))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w3 = w3-lr
                if nnClose<nClose:
                    w3 = w3+lr
            if abs(nClose-(nnClose*w4))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w4 = w4-lr
                if nnClose<nClose:
                    w4 = w4+lr
            
            if nClose - pClose>0:
                if (Open*w1)-pClose<0:
                    w1=w1+lr
            if nClose - pClose<0:
                if (Open*w1)-pClose>0:
                    w1=w1-lr
            
            if nClose - pClose>0:
                if (High*w2)-pClose<0:
                    w2=w2+lr
            if nClose - pClose<0:
                if (High*w2)-pClose>0:
                    w2=w2-lr
            
            if nClose - pClose>0:
                if (Low*w3)-pClose<0:
                    w3=w3+lr
            if nClose - pClose<0:
                if (Low*w3)-pClose>0:
                    w3=w3-lr
            
            if nClose - pClose>0:
                if (pClose*w4)-pClose<0:
                    w4=w4+lr
            if nClose - pClose<0:
                if (pClose*w4)-pClose>0:
                    w4=w4-lr

            N2 = (Open*w5 + High*w6 + Low*w7 + pClose*w8)/4
                  
            if N2>nClose :
                w5 = w5-lr
            if N2<nClose :
                w5 = w5+lr
            if N2>nClose :
                w6 = w6-lr
            if N2<nClose :
                w6 = w6+lr
            if N2>nClose :
                w7 = w7-lr
            if N2<nClose :
                w7 = w7+lr
            if N2>nClose :
                w8 = w8-lr
            if N2<nClose :
                w8 = w8+lr
                        
            if abs(nClose-(Open*w5))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w5 = w5-lr
                if pClose<nClose:
                    w5 = w5+lr
            if abs(nClose-(High*w6))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w6 = w6-lr
                if pClose<nClose:
                    w6 = w6+lr
            if abs(nClose-(Low*w7))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w7 = w7-lr
                if pClose<nClose:
                    w7 = w7+lr
            if abs(nClose-(pClose*w8))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w8 = w8-lr
                if pClose<nClose:
                    w8 = w8+lr
                    
            if abs(nClose-(Open*w5))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w5 = w5-lr
                if nnClose<nClose:
                    w5 = w5+lr
            if abs(nClose-(High*w6))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w6 = w6-lr
                if nnClose<nClose:
                    w6 = w6+lr
            if abs(nClose-(Low*w7))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w7 = w7-lr
                if nnClose<nClose:
                    w7 = w7+lr
            if abs(nClose-(nnClose*w8))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w8 = w8-lr
                if nnClose<nClose:
                    w8 = w8+lr
            
            if nClose - pClose>0:
                if (Open*w5)-pClose<0:
                    w5=w5+lr
            if nClose - pClose<0:
                if (Open*w5)-pClose>0:
                    w5=w5-lr
            
            if nClose - pClose>0:
                if (High*w6)-pClose<0:
                    w6=w6+lr
            if nClose - pClose<0:
                if (High*w6)-pClose>0:
                    w6=w6-lr
            
            if nClose - pClose>0:
                if (Low*w7)-pClose<0:
                    w7=w7+lr
            if nClose - pClose<0:
                if (Low*w7)-pClose>0:
                    w7=w7-lr
            
            if nClose - pClose>0:
                if (pClose*w8)-pClose<0:
                    w8=w8+lr
            if nClose - pClose<0:
                if (pClose*w8)-pClose>0:
                    w8=w8-lr


            N3 = (Open*w9 + High*w10 + Low*w11 + pClose*w12)/4

            if N3>nClose :
                w9 = w9-lr
            if N3<nClose :
                w9 = w9+lr
            if N3>nClose :
                w10 = w10-lr
            if N3<nClose :
                w10 = w10+lr
            if N3>nClose :
                w11 = w11-lr
            if N3<nClose :
                w11 = w11+lr
            if N3>nClose :
                w12 = w12-lr
            if N3<nClose :
                w12 = w12+lr
                    
            if abs(nClose-(Open*w9))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w9 = w9-lr
                if pClose<nClose:
                    w9 = w9+lr
            if abs(nClose-(High*w10))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w10 = w10-lr
                if pClose<nClose:
                    w10 = w10+lr
            if abs(nClose-(Low*w11))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w11 = w11-lr
                if pClose<nClose:
                    w11 = w11+lr
            if abs(nClose-(pClose*w4))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w12 = w12-lr
                if pClose<nClose:
                    w12 = w12+lr
            
            if abs(nClose-(Open*w9))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w9 = w9-lr
                if nnClose<nClose:
                    w9 = w9+lr
            if abs(nClose-(High*w10))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w10 = w10-lr
                if nnClose<nClose:
                    w10 = w10+lr
            if abs(nClose-(Low*w11))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w11 = w11-lr
                if nnClose<nClose:
                    w11 = w11+lr
            if abs(nClose-(nnClose*w4))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w12 = w12-lr
                if nnClose<nClose:
                    w12 = w12+lr
                    
            if nClose - pClose>0:
                if (Open*w9)-pClose<0:
                    w9=w9+lr
            if nClose - pClose<0:
                if (Open*w9)-pClose>0:
                    w9=w9-lr
            
            if nClose - pClose>0:
                if (High*w10)-pClose<0:
                    w10=w10+lr
            if nClose - pClose<0:
                if (High*w10)-pClose>0:
                    w10=w10-lr
            
            if nClose - pClose>0:
                if (Low*w11)-pClose<0:
                    w11=w11+lr
            if nClose - pClose<0:
                if (Low*w11)-pClose>0:
                    w11=w11-lr
            
            if nClose - pClose>0:
                if (pClose*w12)-pClose<0:
                    w12=w12+lr
            if nClose - pClose<0:
                if (pClose*w12)-pClose>0:
                    w12=w12-lr
            
            NN1 =(N1*w13 + N2*w14 + N3*w15)/3

            if NN1>nClose :
                w13 = w13-lr
            if NN1<nClose :
                w13 = w13+lr
            if NN1>nClose :
                w14 = w14-lr
            if NN1<nClose :
                w14 = w14+lr
            if NN1>nClose :
                w15 = w15-lr
            if NN1<nClose :
                w15 = w15+lr
            
            if abs(nClose-(N1*w13))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w13 = w13-lr
                if pClose<nClose:
                    w13 = w13+lr
            
            if abs(nClose-(N2*w14))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w14 = w14-lr
                if pClose<nClose:
                    w14 = w14+lr
            
            if abs(nClose-(N3*w15))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w15 = w15-lr
                if pClose<nClose:
                    w15 = w15+lr
            
            if abs(nClose-(N1*w13))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w13 = w13-lr
                if nnClose<nClose:
                    w13 = w13+lr
            
            if abs(nClose-(N2*w14))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w14 = w14-lr
                if nnClose<nClose:
                    w14 = w14+lr
            
            if abs(nClose-(N3*w15))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w15 = w15-lr
                if nnClose<nClose:
                    w15 = w15+lr
            
            if nClose - pClose>0:
                if (N1*w13)-pClose<0:
                    w13=w13+lr
            if nClose - pClose<0:
                if (N1*w13)-pClose>0:
                    w13=w13-lr
            
            if nClose - pClose>0:
                if (N2*w14)-pClose<0:
                    w14=w14+lr
            if nClose - pClose<0:
                if (N2*w14)-pClose>0:
                    w14=w14-lr
            
            if nClose - pClose>0:
                if (N3*w15)-pClose<0:
                    w15=w15+lr
            if nClose - pClose<0:
                if (N3*w15)-pClose>0:
                    w15=w15-lr

            NN2 =(N1*w16 + N2*w17 + N3*w18)/3

            if NN2>nClose :
                w16 = w16-lr
            if NN2<nClose :
                w16 = w16+lr
            if NN2>nClose :
                w17 = w17-lr
            if NN2<nClose :
                w17 = w17+lr
            if NN2>nClose :
                w18 = w18-lr
            if NN2<nClose :
                w18 = w18+lr
            
            if abs(nClose-(N1*w16))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w16 = w16-lr
                if pClose<nClose:
                    w16 = w16+lr
                    
            if abs(nClose-(N2*w17))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w17 = w17-lr
                if pClose<nClose:
                    w17 = w17+lr
            
            if abs(nClose-(N3*w18))>abs(nClose-pClose)/vol:
                if pClose>nClose:
                    w18 = w18-lr
                if pClose<nClose:
                    w18 = w18+lr
            
            if abs(nClose-(N1*w16))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w16 = w16-lr
                if nnClose<nClose:
                    w16 = w16+lr
                    
            if abs(nClose-(N2*w17))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w17 = w17-lr
                if nnClose<nClose:
                    w17 = w17+lr
            
            if abs(nClose-(N3*w18))>abs(nClose-nnClose)/vol:
                if nnClose>nClose:
                    w18 = w18-lr
                if nnClose<nClose:
                    w18 = w18+lr
                    
            if nClose - pClose>0:
                if (N1*w16)-pClose<0:
                    w16=w16+lr
            if nClose - pClose<0:
                if (N1*w16)-pClose>0:
                    w16=w16-lr
            
            if nClose - pClose>0:
                if (N2*w17)-pClose<0:
                    w17=w17+lr
            if nClose - pClose<0:
                if (N2*w17)-pClose>0:
                    w17=w17-lr
            
            if nClose - pClose>0:
                if (N3*w18)-pClose<0:
                    w18=w18+lr
            if nClose - pClose<0:
                if (N3*w18)-pClose>0:
                    w18=w18-lr
                    
            Output = (NN1+NN2)/2
            delta = s
            s = w1 + w2 + w3 + w4 + w5 + w6 + w7 + w8 + w9 + w10 + w11 + w12 + w13 + w14 + w15 + w16 + w17 + w18
            delta = s-delta
    save = [w1] + [w2] + [w3] + [w4] + [w5] + [w6] + [w7] + [w8] + [w9] + [w10] + [w11] + [w12] + [w13] + [w14] + [w15] + [w16] + [w17] + [w18] + [epoch]
    data = pd.DataFrame(data = save, columns=["weight"])
    data.to_csv('weight.csv', index=True,header=True)


# In[ ]:

def test(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, share, lr):
    print(share)
    url_template = "http://finance.yahoo.com/d/quotes.csv?s={stock}&f=o"
    url = url_template.format(stock=share)
    O = float(max(list(pd.read_csv(url))))

    url_template = "http://finance.yahoo.com/d/quotes.csv?s={stock}&f=h"
    url = url_template.format(stock=share)
    H = float(max(list(pd.read_csv(url))))

    url_template = "http://finance.yahoo.com/d/quotes.csv?s={stock}&f=g"
    url = url_template.format(stock=share)
    L = float(max(list(pd.read_csv(url))))

    url_template = "http://finance.yahoo.com/d/quotes.csv?s={stock}&f=p"
    url = url_template.format(stock=share)
    P = float(max(list(pd.read_csv(url))))
    
    N1 = (O*w1 + H*w2 + L*w3 + P*w4)/4
    N2 = (O*w5 + H*w6 + L*w7 + P*w8)/4
    N3 = (O*w9 + H*w10 + L*w11 + P*w12)/4
    NN1 = (N1*w13 + N2*w14 + N3*w15)/3
    NN2 = (N1*w16 + N2*w17 + N3*w18)/3
    Output = (NN1+NN2)/2
    Output = round(Output, 2)
    Out = str(Output)
    print("Tomorrow's stock price should be £" + Out)


# In[ ]:

if ans == "test" :
    print('Which stock do you want a prediction for? Please enter the ticker here.')
    share = input().upper()
    test(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, share, lr)
    print('Would you like a prediction for another stock?')
    loop = input().lower()


# In[ ]:

if ans == "train":
    print("ok")
    for i in range(300):
        time.sleep(1)
        train(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, s, epoch, vol, delta)
        print(i)
    print(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18)
    print('Do you want to train or test this artificial intelligence?')
    ans = input()


# In[ ]:

if ans == "proof":
    predicted = []
    actual = []
    FTSE =['III.L' , 'ADM.L', 'AAL.L', 'ANTO.L', 'AHT.L', 'ABF.L', 'AZN.L', 'AV.L', 'BAB.L', 'BA.L', 'BARC.L', 'BDEV.L', 'BLT.L', 'BP.L', 'BATS.L', 'BLND.L', 'BT.L', 'BNZL.L', 'BRBY.L', 'CPI.L', 'CCL.L', 'CNA.L', 'CCH.L', 'CPG.L', 'CRH.L', 'DCC.L', 'DGE.L', 'DLG.L', 'DC.L', 'EZJ.L', 'EXPN.L', 'FRES.L', 'GKN.L', 'GSK.L', 'GLEN.L', 'HMSO.L', 'HL.L', 'HIK.L', 'HSBA.L', 'IMB.L', 'INF.L', 'IHG.L', 'IAG.L', 'ITRK.L', 'INTU.L', 'ITV.L', 'SBRY.L', 'JMAT.L', 'KGF.L', 'LAND.L', 'LGEN.L', 'LLOY.L', 'LSE.L', 'MKS.L', 'MDC.L', 'MERL.L', 'MCRO.L', 'MNDI.L', 'NG.L', 'NXT.L', 'OML.L', 'PPB.L', 'PSON.L', 'PSN.L', 'POLY.L', 'PFG.L', 'PRU.L', 'RRS.L', 'RB.L', 'REL.L', 'RIO.L', 'RR.L', 'RBS.L', 'RDSA.L', 'RMG.L', 'RSA.L', 'SGE.L', 'SDR.L', 'SVT.L', 'SHP.L', 'SKY.L', 'SN.L', 'SMIN.L', 'SSE.L', 'STJ.L', 'STAN.L', 'SL.L', 'TW.L', 'TSCO.L', 'TPK.L', 'TUI.L', 'ULVR.L', 'UU.L', 'VOD.L', 'WTB.L', 'MRW.L', 'FERG.L', 'WPG.L', 'WPP.L', 'ABC.L', 'AN.L', 'ASHM.L', 'BBA.L', 'BKG.L', 'BYG.L', 'BVIC.L', 'CHG.L', 'CCC.L', 'DMGT.L', 'DEB.L', 'DLN.L', 'DSG.L', 'DOM.L', 'DRX.L', 'ECM.L', 'ELM.L', 'EIG.L', 'EVR.L', 'FXPO.L', 'FGP.L', 'GNS.L', 'HFD.L', 'HWDN.L', 'HCM.L', 'IAP.L', 'INCH.L', 'JDW.L', 'JD.L', 'KBT.L', 'KAZ.L', 'LAM.L', 'MLD.L', 'MONY.L', 'MPE.L', 'NEX.L', 'OCDO.L', 'PNN.L', 'QQ.L', 'RNK.L', 'RTO.L', 'RMV.L', 'SVS.L', 'SHB.L', 'SHI.L', 'TALK.L', 'VEC.L', 'VSVS.L', 'YOU.L', 'ZYT.L']
    for i in range(149):
        share = FTSE[i]
        Location = r'C:\Users\aksha\Documents\a'+ share + '.csv'
        da = pd.read_csv(Location)
        for i in range(3, len(da)-5):
            Open = float(da['Open'][i-1:i])
            High = float(da['High'][i-1:i])
            Low = float(da['Low'][i-1:i])
            PClose = da['Close'][i-2:i-1]
            NClose = da['Close'][i:i+1]
            nClose = float(NClose)
            pClose = float(PClose)
            Location = r'C:\Users\aksha\Documents\weight.csv'
            df = pd.read_csv(Location)
            w1 = float(df['weight'][0])
            w2 = float(df['weight'][1])
            w3 = float(df['weight'][2])
            w4 = float(df['weight'][3])
            w5 = float(df['weight'][4])
            w6 = float(df['weight'][5])
            w7 = float(df['weight'][6])
            w8 = float(df['weight'][7])
            w9 = float(df['weight'][8])
            w10 = float(df['weight'][9])
            w11 = float(df['weight'][10])
            w12 = float(df['weight'][11])
            w13 = float(df['weight'][12])
            w14 = float(df['weight'][13])
            w15 = float(df['weight'][14])
            w16 = float(df['weight'][15])
            w17 = float(df['weight'][16])
            w18 = float(df['weight'][17])
            N1 = (Open*w1 + High*w2 + Low*w3 + pClose*w4)/4
            N2 = (Open*w5 + High*w6 + Low*w7 + pClose*w8)/4
            N3 = (Open*w9 + High*w10 + Low*w11 + pClose*w12)/4
            NN1 = (N1*w13 + N2*w14 + N3*w15)/3
            NN2 = (N1*w16 + N2*w17 + N3*w18)/3
            Output = (NN1+NN2)/2
            Output = round(Output, 2)
            predicted = predicted + [Output]
            actual = actual + [nClose]
        print(share)
    out = list(zip(predicted, actual))
    df = pd.DataFrame(data = out, columns=["Predicted", "Actual"])
    df.to_csv('proof.csv', index=True,header=True)


# In[ ]:

if ans == "test portfolio" :
    portfolio = ['HSBA.L' , 'FXPO.L', 'CCL.L', 'ULVR.L', 'SDR.L', 'INTU.L', 'RR.L', 'CNA.L', 'UU.L', 'LAM.L']
    for i in range(10):
        share = portfolio[i]
        test(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, share, lr)


# In[ ]:

if ans == "best" :
    FTSE =['III.L' , 'ADM.L', 'AAL.L', 'ANTO.L', 'AHT.L', 'ABF.L', 'AZN.L', 'AV.L', 'BAB.L', 'BA.L', 'BARC.L', 'BDEV.L', 'BLT.L', 'BP.L', 'BATS.L', 'BLND.L', 'BT.L', 'BNZL.L', 'BRBY.L', 'CPI.L', 'CCL.L', 'CNA.L', 'CCH.L', 'CPG.L', 'CRH.L', 'DCC.L', 'DGE.L', 'DLG.L', 'DC.L', 'EZJ.L', 'EXPN.L', 'FRES.L', 'GKN.L', 'GSK.L', 'GLEN.L', 'HMSO.L', 'HL.L', 'HIK.L', 'HSBA.L', 'IMB.L', 'INF.L', 'IHG.L', 'IAG.L', 'ITRK.L', 'INTU.L', 'ITV.L', 'SBRY.L', 'JMAT.L', 'KGF.L', 'LAND.L', 'LGEN.L', 'LLOY.L', 'LSE.L', 'MKS.L', 'MDC.L', 'MERL.L', 'MCRO.L', 'MNDI.L', 'NG.L', 'NXT.L', 'OML.L', 'PPB.L', 'PSON.L', 'PSN.L', 'POLY.L', 'PFG.L', 'PRU.L', 'RRS.L', 'RB.L', 'REL.L', 'RIO.L', 'RR.L', 'RBS.L', 'RDSA.L', 'RMG.L', 'RSA.L', 'SGE.L', 'SDR.L', 'SVT.L', 'SHP.L', 'SKY.L', 'SN.L', 'SMIN.L', 'SSE.L', 'STJ.L', 'STAN.L', 'SL.L', 'TW.L', 'TSCO.L', 'TPK.L', 'TUI.L', 'ULVR.L', 'UU.L', 'VOD.L', 'WTB.L', 'MRW.L', 'FERG.L', 'WPG.L', 'WPP.L', 'ABC.L', 'AN.L', 'ASHM.L', 'BBA.L', 'BKG.L', 'BYG.L', 'BVIC.L', 'CHG.L', 'CCC.L', 'DMGT.L', 'DEB.L', 'DLN.L', 'DSG.L', 'DOM.L', 'DRX.L', 'ECM.L', 'ELM.L', 'EIG.L', 'EVR.L', 'FXPO.L', 'FGP.L', 'GNS.L', 'HFD.L', 'HWDN.L', 'HCM.L', 'IAP.L', 'INCH.L', 'JDW.L', 'JD.L', 'KBT.L', 'KAZ.L', 'LAM.L', 'MLD.L', 'MONY.L', 'MPE.L', 'NEX.L', 'OCDO.L', 'PNN.L', 'QQ.L', 'RNK.L', 'RTO.L', 'RMV.L', 'SVS.L', 'SHB.L', 'SHI.L', 'TALK.L', 'VEC.L', 'VSVS.L', 'YOU.L', 'ZYT.L']
    for i in range(149):
        share = FTSE[i]
        url_template = "http://finance.yahoo.com/d/quotes.csv?s={stock}&f=o"
        url = url_template.format(stock=share)
        O = float(max(list(pd.read_csv(url))))

        url_template = "http://finance.yahoo.com/d/quotes.csv?s={stock}&f=h"
        url = url_template.format(stock=share)
        H = float(max(list(pd.read_csv(url))))

        url_template = "http://finance.yahoo.com/d/quotes.csv?s={stock}&f=g"
        url = url_template.format(stock=share)
        L = float(max(list(pd.read_csv(url))))

        url_template = "http://finance.yahoo.com/d/quotes.csv?s={stock}&f=p"
        url = url_template.format(stock=share)
        P = float(max(list(pd.read_csv(url))))
        
        N1 = (O*w1 + H*w2 + L*w3 + P*w4)/4
        N2 = (O*w5 + H*w6 + L*w7 + P*w8)/4
        N3 = (O*w9 + H*w10 + L*w11 + P*w12)/4
        NN1 = (N1*w13 + N2*w14 + N3*w15)/3
        NN2 = (N1*w16 + N2*w17 + N3*w18)/3
        Output = (NN1+NN2)/2
        Output = round(Output, 2)
        Change = 100*((Output-O)/O)
        List = List + [Change]
        print(i)
        time.sleep(1)
    
    out = list(zip(List, FTSE))
    out = sorted(out)
    df = pd.DataFrame(data = out, columns=["Change", "Ticker"])
    print(df)


# In[ ]:

if ans == "test" :
    print('Which stock do you want a prediction for? Please enter the ticker here.')
    share = input().upper()
    test(w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14, w15, w16, w17, w18, share, lr)
    print('Would you like a prediction for another stock?')

