# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['news.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('send.py', '.'),  
        ('check.py', '.'),   
        ('logo.png', '.'),
        ('last_hash.txt', '.')
    ],
    hiddenimports=['requests','beautifulsoup4','smtplib','Pillow'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
    cipher=block_cipher

)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='news',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='news'
)