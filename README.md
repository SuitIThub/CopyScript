# FileFlow
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Pillow](https://img.shields.io/badge/Pillow-9.0.0+-green.svg)](https://python-pillow.org/)
[![Watchdog](https://img.shields.io/badge/Watchdog-3.0.0-orange.svg)](https://pypi.org/project/watchdog/)
[![Platform](https://img.shields.io/badge/platform-windows%20%7C%20linux%20%7C%20macos-lightgrey.svg)](https://github.com/yourusername/FileFlow)

## File Manager with Advanced Rule-based Renaming

A Python GUI application that monitors a source folder for newly created files and copies them to a destination folder with sophisticated rule-based renaming patterns. Features a modern interface with thumbnails, multiple viewing modes, and comprehensive file management capabilities.

## Features

### Core Functionality
- **Real-time File Monitoring**: Uses watchdog library to monitor source folder for new files
- **Advanced Rule-based Renaming**: Create complex naming patterns using configurable rules with tags
- **Smart File Handling**: Waits for files to finish writing before tracking them
- **Visual Feedback**: Clear status indicators and tooltips throughout the interface

### File Management
- **Thumbnail Previews**: Automatic thumbnail generation for images with fallbacks for other file types
- **Multiple View Modes**: Switch between list view and grid view for tracked files
- **File Reordering**: Move files up/down in the processing order
- **Individual File Removal**: Remove specific files from tracking list
- **Conflict Detection**: Warns about duplicate filenames and existing files in destination

### Rule System
Three powerful rule types with advanced controls:

- **Counter Rule**: 
  - Increments with each file processed
  - Configurable start value, increment amount
  - Step control (increment every N operations)
  - Maximum value with wraparound support

- **List Rule**: 
  - Cycles through predefined values
  - Step control (advance to next value every N operations)
  - Configurable list of values (semicolon-separated)

- **Batch Rule**: 
  - Persists across batch operations
  - Increments with each "Copy & Rename" operation
  - Step and maximum value controls
  - Maintains state between application sessions

### User Interface
- **Intuitive Tooltips**: Comprehensive help text for all controls
- **Visual Path Validation**: ✅/❌ indicators for folder paths with auto-create buttons
- **Smart Button States**: Context-aware enabling/disabling of controls
- **Real-time Preview**: See generated filenames before copying
- **Progress Feedback**: Clear status messages and conflict warnings

### Settings Management
- **Auto-save**: Settings automatically saved on application close
- **Import/Export**: Share configurations between instances
- **Persistent State**: Batch counters and settings maintained across sessions

## Installation

1. Ensure Python 3.6+ is installed
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Initial Setup
1. Run the application:
   ```bash
   python copy_script.py
   ```

2. **Configure Folders**:
   - **Source Folder**: Select where new files will be monitored
   - **Destination Folder**: Where renamed files will be copied
   - Both paths show ✅ when valid, ❌ when invalid, with auto-create buttons

3. **Set File Formats** (optional):
   - Enter extensions like `.jpg;.png;.gif` or use `*` for all files
   - Filters which files get tracked automatically

### Creating Naming Rules

4. **Design Naming Pattern**:
   - Use `{tag_name}` placeholders in your pattern
   - Example: `photo_{batch}_{counter}_{type}`
   - Pattern label shows ⚠️ if tags lack corresponding rules

5. **Add Rules**:
   - Click "Add Rule" to create counter, list, or batch rules
   - Each rule corresponds to a tag in your naming pattern
   - Configure advanced options like step intervals and maximum values

### File Processing

6. **Start Tracking**:
   - Click "Start Tracking" to begin monitoring
   - Only files created after starting are tracked
   - View tracked files in list or grid mode with thumbnails

7. **Manage Tracked Files**:
   - Reorder files using up/down arrows
   - Remove individual files with delete buttons
   - Preview generated names in real-time

8. **Copy & Rename**:
   - Review any conflicts or warnings
   - Choose how to handle existing files (overwrite, skip, or cancel)
   - Files are processed and tracked list is cleared

## Rule Examples

### Photo Organization
```
Pattern: vacation_{batch}_{counter}
Rules:
- Counter: tag="counter", start=1, step=1
- Batch: tag="batch", start=1, step=1

Result: vacation_1_1.jpg, vacation_1_2.jpg, vacation_1_3.jpg
After next batch: vacation_2_1.jpg, vacation_2_2.jpg, vacation_2_3.jpg
```

### Alternating Categories
```
Pattern: doc_{type}_{counter}
Rules:
- List: tag="type", values="report;summary;draft", step=2
- Counter: tag="counter", start=1, step=1

Result: doc_report_1.pdf, doc_report_2.pdf, doc_summary_3.pdf, doc_summary_4.pdf, doc_draft_5.pdf
```

### Advanced Cycling
```
Pattern: item_{category}_{num}
Rules:
- List: tag="category", values="A;B;C", step=1
- Counter: tag="num", start=0, increment=1, max=2

Result: item_A_0.txt, item_B_1.txt, item_C_2.txt, item_A_0.txt, item_B_1.txt...
```

## Advanced Features

### File Conflict Handling
- **Duplicate Prevention**: Detects when multiple files would have the same name
- **Existing File Warnings**: Shows which destination files would be overwritten
- **Flexible Actions**: Choose to overwrite, skip, or cancel for existing files

### Visual Feedback
- **Path Validation**: Real-time validation of source and destination paths
- **Missing Rules Warning**: Highlights when naming pattern uses undefined tags
- **Thumbnail Generation**: Automatic image previews with retry logic for locked files
- **Status Updates**: Clear feedback during all operations

### View Modes
- **List View**: Compact display with filename, preview name, and controls
- **Grid View**: Thumbnail-focused layout for visual file management
- **Seamless Switching**: Toggle between views without losing state

## Settings File Structure

The application saves settings to `file_manager_settings.json`:

```json
{
  "source_folder": "/path/to/source",
  "dest_folder": "/path/to/destination", 
  "file_formats": ".jpg;.png",
  "naming_pattern": "photo_{batch}_{counter}",
  "rules": [
    {
      "type": "counter",
      "tag_name": "counter",
      "start_value": 1,
      "increment": 1,
      "step": 1,
      "max_value": null
    }
  ]
}
```

## Dependencies

- `tkinter`: GUI framework (built into Python) - [docs.python.org/3/library/tkinter.html](https://docs.python.org/3/library/tkinter.html)
- `watchdog`: File system monitoring - [pypi.org/project/watchdog](https://pypi.org/project/watchdog/)
- `Pillow`: Image processing and thumbnail generation - [pillow.readthedocs.io](https://pillow.readthedocs.io/)
- `pathlib`: Modern path handling - [docs.python.org/3/library/pathlib.html](https://docs.python.org/3/library/pathlib.html)

## Troubleshooting

### Common Issues
- **Files not tracking**: Ensure source folder is valid and tracking is started
- **Permission errors**: Check read access to source and write access to destination
- **Thumbnails not generating**: May indicate locked or corrupted image files
- **Rules not working**: Verify tag names in pattern match rule tag names exactly

### Performance Notes
- Thumbnails are cached for better performance
- Large batches may take time for thumbnail generation
- File system monitoring has small delays to ensure files are completely written

## File Structure

```
copy_script.py                   # Main application
requirements.txt                 # Python dependencies  
file_manager_settings.json       # Auto-generated settings (created on first run)
README.md                       # This documentation
```

## Tips

- **File Extensions**: Original extensions are always preserved
- **Batch Persistence**: Batch counters maintain state between sessions
- **Rule Order**: Rules are processed in the order they appear in your pattern
- **Preview Names**: Use the preview to verify naming before copying
- **Backup Important Files**: Always test with non-critical files first 