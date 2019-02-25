# -*- mode: python -*-

block_cipher = None


a = Analysis(['device_identifier.py'],
             pathex=['/Users/dhuang/gdrive/dev/netdisco-python-wrapper'],
             binaries=[],
             datas=[('netdisco/discoverables/*.py', 'netdisco/discoverables')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='device_identifier',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
