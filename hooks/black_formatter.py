#!/usr/bin/env python3
"""
Auto-format Python files with Black after edits.
Non-blocking - continues even if formatting fails.
"""

import json
import sys
import subprocess
from pathlib import Path

def is_python_file(file_path):
    """Check if the file is a Python file."""
    if not file_path:
        return False
    
    path = Path(file_path)
    return path.suffix in ['.py', '.pyi', '.pyx']

def format_with_black(file_path):
    """Format the file with Black."""
    try:
        result = subprocess.run(
            ['black', file_path, '--quiet'],
            capture_output=True,
            text=True,
            timeout=10
        )
        
        if result.returncode == 0:
            print(f"✅ Formatted {file_path} with Black", file=sys.stderr)
        elif result.stderr:
            print(f"⚠️  Black formatting issue: {result.stderr}", file=sys.stderr)
            
    except subprocess.TimeoutExpired:
        print(f"⚠️  Black formatting timed out for {file_path}", file=sys.stderr)
    except FileNotFoundError:
        # Black not installed - silently continue
        pass
    except Exception as e:
        print(f"⚠️  Black formatting error: {e}", file=sys.stderr)

def main():
    try:
        # Read input from stdin
        input_data = json.load(sys.stdin)
        
        tool_name = input_data.get('tool', '')
        
        # Only process Edit and Write tools
        if tool_name not in ['Edit', 'Write']:
            sys.exit(0)
        
        file_path = input_data.get('file_path', '')
        
        # Only format Python files
        if not is_python_file(file_path):
            sys.exit(0)
        
        # Format the file (non-blocking)
        format_with_black(file_path)
        
        # Always exit successfully (non-blocking)
        sys.exit(0)
        
    except Exception:
        # Don't block on any errors
        sys.exit(0)

if __name__ == "__main__":
    main()