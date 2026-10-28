"""
Create portable ZIP package for Any Torrent
"""

import os
import shutil
import zipfile
from pathlib import Path

def create_portable_package():
    print("="*70)
    print("  Creating Portable Package")
    print("="*70)
    
    base_dir = Path(__file__).parent.parent
    dist_dir = base_dir / "dist"
    
    # Files to include
    exe_file = dist_dir / "AnyTorrent" / "AnyTorrent.exe"
    if not exe_file.exists():
        exe_file = dist_dir / "AnyTorrent.exe"
    readme_file = base_dir / "docs" / "README_PORTABLE.txt"
    
    # Check if exe exists
    if not exe_file.exists():
        print(f"✗ Error: {exe_file} not found")
        print("  Please build the executable first using: python scripts/build_exe.py")
        return False
    
    # Output ZIP file
    zip_name = "AnyTorrent_Portable.zip"
    zip_path = dist_dir / zip_name
    
    # Remove old zip if exists
    if zip_path.exists():
        zip_path.unlink()
        print(f"✓ Removed old {zip_name}")
    
    # Create the ZIP
    print(f"\n📦 Creating {zip_name}...")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # Add the executable
        zipf.write(exe_file, "AnyTorrent.exe")
        print(f"  ✓ Added AnyTorrent.exe ({exe_file.stat().st_size / (1024*1024):.2f} MB)")
        
        # Add README if exists
        if readme_file.exists():
            zipf.write(readme_file, "README.txt")
            print(f"  ✓ Added README.txt")
        else:
            # Create a simple readme inside the zip
            readme_content = """Any Torrent - Portable Version

HOW TO USE:
1. Extract this ZIP file to any folder
2. Double-click AnyTorrent.exe to run
3. No installation needed!

FEATURES:
- Search multiple torrent sites
- Built-in torrent downloader
- Beautiful modern interface
- Completely portable - run from USB drive!

REQUIREMENTS:
- Windows 10 or later
- No additional software needed

For more info visit: https://github.com/sayandey021

Enjoy! 🚀
"""
            zipf.writestr("README.txt", readme_content)
            print(f"  ✓ Added README.txt")
    
    # Summary
    zip_size = zip_path.stat().st_size / (1024*1024)
    print(f"\n{'='*70}")
    print(f"✅ Portable package created successfully!")
    print(f"{'='*70}")
    print(f"📦 Package: {zip_path}")
    print(f"📊 Size: {zip_size:.2f} MB")
    print(f"\n💡 This is ready to distribute to users!")
    print(f"   Users just extract and double-click AnyTorrent.exe")
    print(f"{'='*70}")
    
    return True

if __name__ == "__main__":
    create_portable_package()
