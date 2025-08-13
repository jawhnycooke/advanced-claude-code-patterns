#!/usr/bin/env python3
"""
Log tool usage for audit and debugging purposes.
"""

import json
import sys
from datetime import datetime
from pathlib import Path

def main():
    try:
        # Read input from stdin
        input_data = json.load(sys.stdin)
        
        # Extract relevant information
        tool_name = input_data.get('tool', 'unknown')
        session_id = input_data.get('sessionId', 'unknown')
        
        # Create log entry
        log_entry = {
            'timestamp': datetime.now().isoformat(),
            'session_id': session_id,
            'tool': tool_name,
            'data': {}
        }
        
        # Add tool-specific data
        if tool_name == 'Bash':
            log_entry['data']['command'] = input_data.get('command', '')
            log_entry['data']['description'] = input_data.get('description', '')
        elif tool_name in ['Edit', 'Write']:
            log_entry['data']['file_path'] = input_data.get('file_path', '')
        elif tool_name in ['Read', 'Grep', 'Glob']:
            log_entry['data']['path'] = input_data.get('path', '')
            if tool_name == 'Grep':
                log_entry['data']['pattern'] = input_data.get('pattern', '')
        
        # Ensure .claude directory exists
        claude_dir = Path('.claude')
        claude_dir.mkdir(exist_ok=True)
        
        # Log file path
        log_file = claude_dir / 'tool_usage.json'
        
        # Load existing logs or create new list
        if log_file.exists():
            with open(log_file, 'r') as f:
                logs = json.load(f)
        else:
            logs = []
        
        # Append new log entry
        logs.append(log_entry)
        
        # Save updated logs
        with open(log_file, 'w') as f:
            json.dump(logs, f, indent=2)
        
        # Exit successfully
        sys.exit(0)
        
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON input: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()