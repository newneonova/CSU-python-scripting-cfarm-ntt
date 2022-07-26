# INV2018 DayCent .100 Files
# 11/21/19

# THIS FOLDER RENAMED FROM: INV2018_Yao30cm TO INV2018

# *** FOR Running Full Inventory

# 1) Copied .100 files from INV2015 Folder
# 2) Copied Ram's Fix.100 & added F-T to bottom from Ken's 
     Rams: RAM_Final_30cm_fix.100
     Kens: Kens_fixm07_30.100
       from: N:\Public\RubelScratch\rubelogle\kendrick\2018Inventory
# 3) New 100 Files from S.W. (see below)
# 4) Uses new CROP.100 from S.W. w/FALW
# 5) Uses OMAD.100 from E.M. for INV2015 SchlFiles


NOTE: Diff btwn Ken's Kens_fixm07_30.100 & Yao's fix.100
      1) Yao has WEFF(1) & WEFF(2) @ line 160-161
      2) Ken has WEFF(1) & WEFF(2) @ line 231-232
         Line 230 is an extra commnet about Eff of Water Decomp         
         ** KEN has WEFF(1) Commented-out
         Values are the same btwn Yao & Ken

  
1/14/20:

- Added an OMAD.100 file that sets all OMADs to an OMADTYP = 1.0
- Original OMAD.100 file (used in INV runs) had OMADTYP = 1.5 
  for OMAD events (PRP events are OMADTYP = 1.0) (omad_MAIN_TYP1.5.100)
- File Name: omad_OMADTYP10.100
- Used to test diff between OMADTYP 1.5 & 1.0


1/13/20:

- Added a FIX.100 file that comments-out the Freeze-Thaw parameters
- File Name: fix_NO_FT.100
- Used to test diff btwn FT & NO FT
- Main INV 2018 Run used FT (fix_MAIN_wFT.100)
 

11/21/19:

- Ram & S.W. provided a new & updated CULT.100 file
- This replaced the old CULT.100

  
11/7/19:

- Updated CROP.100 set CROP 'WC3' HIMAX = 0.02
         
11/1/19:

- Added new files from S.W. with minor changes 
- CULT.100: S.W.Corrected parameter names in two events SHRD & CULT
  + Added parentheses & quotes to these events since they were missing
  + S.W. deleted PINE (for pineapple) since not really needed in INV
- HARV.100: S.W. Corrected parameter names in two events
  + Added quotes to several events since they were missing
  + HARV event 'GS' copied to 'G50S' so that both are in there
- CROP.100: S.W. has revised grass & grass legume crops
  + also includes 'FALW' & updated 'RYE' crop
- RAM & S.W. approved the fix.100 file status
- Final FLN20R = 100.0 in fix.100

         
10/30/19:

- Use Yao's fix.100
- Set fix.100 Parameter FLN20R = 100.0
- Added 'MLRA' event to OMAD.100

10/28/19: 

- TEST fix.100 setting FLN20R = 1000.0
  + This is the value used in Ken's Kens_fixm07_30.100 File
  + Save in Tables w/ Pattern 30cm1000_N2N2O_102819
  

10/27/19:

- RAN fix.100 FROM YAO w/ FLN20R = 100.0
- Test runs show that BH SchlFiles use 'MLRA' OMAD.100 Event
  + this was missing in new OMAD.100 file
- I added this event for now to the OMAD.100 file from the INV2015 OMAD.100 file



ORIGINAL NOTES from INV2018 100 File Folder

10/21/19:

- CROP.100 received from Steve Williams to add new crop for Fallow: 'FALW'
- FALW is a new crop type to be used in Inventory 2018


10/18/19:

- OMAD.100 received from Ernie Marx to add new OMAD definitions to be used with the Inventory 2018 Schl Files

- Two Files Added by Ram G. for the 30cm Version TO BE USED FOR Inventory 2018
  + These are not yet ready to use so they are named:
    - RAM_Final_30cm_cult.100
    - RAM_Final_30cm_fix.100
  + Once the 30cm DayCent Branch is integrated these files will become the new cult.100 & fix.100 files
  + Notes from Ram:
  
  I have attached a fix.100 and cult.100 files for the optimized 30cm version of the model. These parameter sets are considered the best set with the highest posterior density. The cult.100 might be a limited version and I only updated cult A-K and others were the same as before. I did not change sitepar.in or the crop.100 parameters during the parameterization and should be the same as last year's inventory files. Let me know if you have any questions. 