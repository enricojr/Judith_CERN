import ROOT

#-----------------------------------------------------------------------------
# Load necessary shared libraries
#
def setPlotDefaults(root, options = None):

    #root.gROOT.SetStyle('Plain')

    root.gStyle.SetFillColor(10)           
    root.gStyle.SetFrameFillColor(10)      
    root.gStyle.SetCanvasColor(10)         
    root.gStyle.SetPadColor(10)            
    root.gStyle.SetTitleFillColor(0)       
    root.gStyle.SetStatColor(10)   
    
    root.gStyle.SetCanvasBorderMode(0)
    root.gStyle.SetFrameBorderMode(0) 
    root.gStyle.SetPadBorderMode(0)   
    root.gStyle.SetDrawBorder(0)      
    root.gStyle.SetTitleBorderSize(0)
    
    root.gStyle.SetFuncWidth(2)
    root.gStyle.SetHistLineWidth(2)
    root.gStyle.SetFuncColor(2)
    
    root.gStyle.SetPadTopMargin(0.08)
    root.gStyle.SetPadBottomMargin(0.16)
    root.gStyle.SetPadLeftMargin(0.16)
    root.gStyle.SetPadRightMargin(0.12)
  
    # set axis ticks on top and right
    root.gStyle.SetPadTickX(1)         
    root.gStyle.SetPadTickY(1)         
  
    # Set the background color to white
    root.gStyle.SetFillColor(10)           
    root.gStyle.SetFrameFillColor(10)      
    root.gStyle.SetCanvasColor(10)         
    root.gStyle.SetPadColor(10)            
    root.gStyle.SetTitleFillColor(0)       
    root.gStyle.SetStatColor(10)           
  
  
    # Turn off all borders
    root.gStyle.SetCanvasBorderMode(0)
    root.gStyle.SetFrameBorderMode(0) 
    root.gStyle.SetPadBorderMode(0)   
    root.gStyle.SetDrawBorder(0)      
    root.gStyle.SetTitleBorderSize(0) 
  
    # Set the size of the default canvas
    root.gStyle.SetCanvasDefH(400)          
    root.gStyle.SetCanvasDefW(650)          
    #gStyle->SetCanvasDefX(10)
    #gStyle->SetCanvasDefY(10)   
  
    # Set fonts
    font = 42
    #root.gStyle.SetLabelFont(font,'xyz')
    #root.gStyle.SetStatFont(font)       
    #root.gStyle.SetTitleFont(font)      
    #root.gStyle.SetTitleFont(font,'xyz')
    #root.gStyle.SetTextFont(font)       
    #root.gStyle.SetTitleX(0.3)        
    #root.gStyle.SetTitleW(0.4)        
  
   # Set Line Widths
   #gStyle->SetFrameLineWidth(0)
   #root.gStyle.SetFuncWidth(2)
   #root.gStyle.SetHistLineWidth(2)
   #root.gStyle.SetFuncColor(2)
   #
   # Set tick marks and turn off grids
    root.gStyle.SetNdivisions(505,'xyz')
   #
   # Set Data/Stat/... and other options
   #root.gStyle.SetOptDate(0)
   #root.gStyle.SetDateX(0.1)
   #root.gStyle.SetDateY(0.1)
   #gStyle->SetOptFile(0)
   ##root.gStyle.SetOptStat(1110)
    root.gStyle.SetOptStat(1111)
    #root.gStyle.SetOptFit(111)
    root.gStyle.SetStatFormat('4.3f')
    root.gStyle.SetFitFormat('4.3f')
   #gStyle->SetStatTextColor(1)
   #gStyle->SetStatColor(1)
   #gStyle->SetOptFit(1)
   #gStyle->SetStatH(0.20)
   #gStyle->SetStatStyle(0)
   #gStyle->SetStatW(0.30)
   #gStyle -SetStatLineColor(0)
   #root.gStyle.SetStatX(0.919)
   #root.gStyle.SetStatY(0.919)
   #root.gStyle.SetOptTitle(0)
   #gStyle->SetStatStyle(0000)    # transparent mode of Stats PaveLabel
   #root.gStyle.SetStatBorderSize(0)
   #
    #root.gStyle.SetLabelSize(0.065,'xyz')
    #gStyle -> SetLabelOffset(0.005,'xyz')
    #root.gStyle.SetTitleY(.5)
    root.gStyle.SetTitleOffset(1.0,'xz')
    root.gStyle.SetTitleOffset(1.1,'y')
    root.gStyle.SetTitleSize(0.065, 'xyz')
    root.gStyle.SetLabelSize(0.065, 'xyz')
    #root.gStyle.SetTextAlign(22)
    root.gStyle.SetTextSize(0.1)
   #
   ##root.gStyle.SetPaperSize(root.TStyle.kA4)  
    root.gStyle.SetPalette(1)
   #
   ##root.gStyle.SetHistMinimumZero(True)
   
    root.gROOT.ForceStyle()
#-----------------------------------------
def Format(h):

    h.SetLineColor(1)
    h.SetMarkerColor(1)
    h.SetTitle('Projection of 2D Efficiency')
#-----------------------------------------
def Style():
    ROOT.gROOT.LoadMacro('/Users/schae/testarea/CAFAna/HWWMVACode/atlasstyle-00-03-05/AtlasStyle.C')                   
    ROOT.gROOT.LoadMacro('/Users/schae/testarea/CAFAna/HWWMVACode/atlasstyle-00-03-05/AtlasUtils.C')
    ROOT.SetAtlasStyle()

def Fit(file_name='',_suffix=''):
    #f = ROOT.TFile.Open('./../Judith_original/TestData/dut-60V_runs-2-3-4-5-6-7-1-4-5-6_settings1_sync_analysis-result.root')
    #f = ROOT.TFile.Open('./../Judith_original/TestData/dut-120V_runs-23-24-25-26-27-28-29-30-1-2-3-4-5-6-7_settings1_sync_analysis-result-cutslope.root')
    #f = ROOT.TFile.Open('./../Judith_original/TestData/dut-90V_runs-9-11-1-2-3-5-6-8-9_settings_sync_analysis-result.root')
    #f = ROOT.TFile.Open('./../Judith_original/TestData/dut-120V_runs-23-24-25-26-27-28-29-30-1-2-3-4-5-6-7_settings1_sync_analysis-result.root')
    #f = ROOT.TFile.Open('./../Judith_original/TestData/dut-90V_runs-9-11-1-2-3-5-6-8-9_settings_sync_analysis-result-nocut-align.root')
    f = ROOT.TFile.Open(file_name)
    #dut-60V_runs-2-3-4-5-6-7-1-4-5-6_settings1_sync_analysis-result-cutt0-align.root
    #dut-120V_runs-23-24-25-26-27-28-29-30-1-2-3-4-5-6-7_settings1_sync_analysis-result-nocut-align.root
    #f = ROOT.TFile.Open('./../Judith_original/TestData/dut-120V_runs-23-24-25-26-27-28-29-30-1-2-3-4-5-6-7_settings1_sync_analysis-result.root')
    #twoD = f.Get('Efficiency/sensor0_TrackResEffFine')
    twoD = f.Get('Efficiency/DUTPlane0TrackResidualHitFine')
    twoDall = f.Get('Efficiency/DUTPlane0TrackResidualFine')        
    DoX=False
    can = ROOT.TCanvas("c2","c2",100,10,800,600);
    can.cd()
    twoD.Draw('colz')
    can.Update()
    can.WaitPrimitive() 
    t1 = raw_input('input the x shift. typically the x-mean: ')
    t2 = raw_input('input the y shift. typically the y-mean: ')

    xshift = float(t1)
    yshift = float(t2)
    bin_width=5
    #bin_width=15
    midX=twoD.GetNbinsX()/2+int(xshift)
    midY=twoD.GetNbinsY()/2+int(yshift)
    midX_noshift=twoD.GetNbinsX()/2
    midY_noshift=twoD.GetNbinsY()/2

    if DoX:
        xshift=0
    else:
        yshift=0
    
    proj = ROOT.TH1F('proj','',int(twoD.GetNbinsX()/bin_width),twoD.GetXaxis().GetBinLowEdge(0),twoD.GetXaxis().GetBinUpEdge(twoD.GetNbinsX()))
    
    for q in range(0,int(twoD.GetNbinsX()/float(bin_width))):
        mysum = 0.0
        entries = 0.0
        for i in range(q*bin_width,(q+1)*bin_width):
            for j in range(-10,11):
                if DoX:
                    mysum+=twoD.GetBinContent(i+int(xshift),midY+j)
                    entries+=twoDall.GetBinContent(i+int(xshift),midY+j)
                else:
                    mysum+=twoD.GetBinContent(midX+j,i+int(yshift))
                    entries+=twoDall.GetBinContent(midX+j,i+int(yshift))                    
        if entries==0.0:
            entries+=1.0
        #proj.SetBinContent(q,mysum/entries/0.97)
        proj.SetBinContent(q,mysum) 
        proj.SetBinError(q,0.0)        
    proj.GetXaxis().SetRangeUser(-100,100)
    #proj.SetTitle('DUT Hit Efficiency')
    if DoX:
        proj.GetXaxis().SetTitle('x Residual [#mum]')
    else:
        proj.GetXaxis().SetTitle('y Residual [#mum]')
    proj.GetYaxis().SetTitle('Fractional DUT Hit Efficiency')
    proj.SetTitle('')
    proj.SetStats(0)
    proj.SetLineWidth(2)
    proj.SetLineColor(1)
    proj.SetMarkerColor(1)    
    proj.Draw()
    can.Update()
    can.WaitPrimitive()
    raw_input('Waiting for you to finish editting')
    if DoX:
        can.SaveAs('efficiencyProjX_'+_suffix+'.eps')
        can.SaveAs('efficiencyProjX_'+_suffix+'.pdf')
        can.SaveAs('efficiencyProjX_'+_suffix+'.C')
    else:
        can.SaveAs('efficiencyProjY_'+_suffix+'.eps')
        can.SaveAs('efficiencyProjY_'+_suffix+'.pdf')
        can.SaveAs('efficiencyProjY_'+_suffix+'.C')        


#Style()
setPlotDefaults(ROOT)
#Fit('60V')
#Fit('./../Judith_original/TestData/dut-60V_runs-2-3-4-5-6-7-1-4-5-6_settings1_sync_analysis-result-cutt0wider-align.root','cutt0_60V')
#Fit('./../Judith_original/TestData/dut-90V_runs-9-11-1-2-3-5-6-8-9_settings_sync_analysis-result-cutt0wider-align.root','cutt0_90V')
#Fit('./../Judith_original/TestData/dut-120V_runs-23-24-25-26-27-28-29-30-1-2-3-4-5-6-7_settings1_sync_analysis-result-cutt0wider-align.root','cutt0_120V')
Fit('TowerJazz/dut_run804_sync-analysis-result.root','No Cut')

#Fit('./../Judith_original/TestData/dut-60V_runs-2-3-4-5-6-7-1-4-5-6_settings1_sync_analysis-result-nocut-align.root','nocut_60V')
#Fit('./../Judith_original/TestData/dut-90V_runs-9-11-1-2-3-5-6-8-9_settings_sync_analysis-result-nocut-align.root','nocut_90V')
#Fit('./../Judith_original/TestData/dut-120V_runs-23-24-25-26-27-28-29-30-1-2-3-4-5-6-7_settings1_sync_analysis-result-nocut-align.root','nocut_120V')
#
#Fit('./../Judith_original/TestData/dut-60V_runs-2-3-4-5-6-7-1-4-5-6_settings1_sync_analysis-result-cutslope-align.root','cutslope_60V')
#Fit('./../Judith_original/TestData/dut-90V_runs-9-11-1-2-3-5-6-8-9_settings_sync_analysis-result-cutslope-align.root','cutslope_90V')
#Fit('./../Judith_original/TestData/dut-120V_runs-23-24-25-26-27-28-29-30-1-2-3-4-5-6-7_settings1_sync_analysis-result-cutslope-align.root','cutslope_120V')
