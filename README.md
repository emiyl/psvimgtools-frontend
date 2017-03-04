# psvimgtools-frontend
This is a GUI Interface For Team Molecule / Yifanlu's PSVIMGTools 
Which is a tool that can be used to decrypt & extract PSVita Backup Files (.psvimg) Providing you knew the AID of the account that created the backup, 

this works on every firmware to this date, including 3.63. and probably all future firmwares

the only problem with yifan's inital release, was it was a command-line only tool and also could be a pain in the ass to some unexperienced users, so this is where i came in and decided to make this GUI Frontend which will give you all the functions of psvimgtools + more with a GUI. My frontend was written in Python2.7 and supports windows and linux 64-Bit 
(32-bit is NOT Supported, this is a because of yifanlu's tools not mine) keep in mind that for linux you require libgcrypt11-dev to be installed (sudo apt-get install libgcrypt11-dev) also for everyone, qcma is required for this app to even run.

To design the GUI's i used a tool called PAGE that made it much faster for me to generate GUIS

Now i think i should mention some features i have for this:

1. QCMA Intergration. i have tried my best to make this intergrate well with QCMA. For example when you start the app for the first time it will automatically find your QCMA Backups Folder, and will Automatically find your accounts AID, and download CMA Key You can also trigger both of these process'es to occur manually.

2. Quick Resign, Quickly Change the owner of a backup (Note: Only DRMFree Content will run on incorrect accounts!)

3. Extract and Create Backup Files

4. EasyInstallers, Enables you to easily install, Hidden Applications, ARK-2, VHBL Whitelist Hack, And URICaller i do plan on adding more options to this later.

5. Account Mannager, save multiple accounts's AID, and KEY's

6. Reading Param.SFO File To display backup NAME instead of TITLEID

I also have a few features planned such as:

1. Some sort of progress bar/indicator

2. Remove 'Topics' app Easyinstalelr

For noobs: No this doesnt enable piracy, (except for epsp..) And No this isnt goint to lead to a 3.63 spoof for games or PSN.

