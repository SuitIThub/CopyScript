#!/usr/bin/env python3
"""
Script to create a Windows shortcut (.lnk) file for the File Manager application.
Run this once to create the shortcut, then use the shortcut in FlexBar.
"""

import os
import sys

try:
    import win32com.client
except ImportError:
    print("Error: pywin32 package is required to create shortcuts.")
    print("Install it with: pip install pywin32")
    sys.exit(1)

def create_shortcut():
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Define paths
    target_script = os.path.join(script_dir, "copy_script.py")
    shortcut_path = os.path.join(script_dir, "File Manager.lnk")
    
    # Create shortcut
    shell = win32com.client.Dispatch("WScript.Shell")
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = sys.executable  # Python executable
    shortcut.Arguments = f'"{target_script}"'
    shortcut.WorkingDirectory = script_dir
    shortcut.IconLocation = sys.executable
    shortcut.Description = "File Manager with Rule-based Renaming"
    shortcut.save()
    
    print(f"Shortcut created: {shortcut_path}")
    print(f"Target: {sys.executable} {target_script}")
    print(f"Working Directory: {script_dir}")
    print("\nUse this shortcut path in FlexBar:")
    print(f'"{shortcut_path}"')

if __name__ == "__main__":
    create_shortcut() 