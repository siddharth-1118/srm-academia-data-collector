# SRM Academia Data Collector

A Python script to collect academic data from SRM Academia using the Vcademia API. This tool allows you to export your student details, attendance, marks, courses, and timetable to CSV, JSON, and Excel formats.

## Features

- ✅ **Secure Authentication**: Prompts for credentials at runtime (no hardcoded passwords)
- ✅ **Comprehensive Data Collection**: 
  - Student Details
  - Attendance Records
  - Marks/Grades
  - Course Information
  - Timetable
- ✅ **Multiple Export Formats**: JSON, CSV, and Excel
- ✅ **Timestamped Files**: All exports include timestamps for organization
- ✅ **Error Handling**: Graceful error handling and informative messages

## Prerequisites

- Python 3.7 or higher
- SRM Academia account credentials

## Installation

1. **Clone the repository**:

```bash
git clone https://github.com/siddharth-1118/srm-academia-data-collector.git
cd srm-academia-data-collector
```

2. **Install required packages**:

```bash
pip install -r requirements.txt
```

## Usage

1. **Run the script**:

```bash
python academia_scraper.py
```

2. **Enter your credentials** when prompted:
   - Email: Your SRM email (e.g., `sv3814@srmist.edu.in`)
   - Password: Your SRM Academia password

3. **Wait for data collection**: The script will:
   - Authenticate with the Vcademia API
   - Fetch all available data
   - Export to multiple formats

4. **Find your data**: Exported files will be saved in the same directory:
   - `academia_data_YYYYMMDD_HHMMSS.json` - Complete data in JSON format
   - `student_YYYYMMDD_HHMMSS.csv` - Student details
   - `attendance_YYYYMMDD_HHMMSS.csv` - Attendance records
   - `marks_YYYYMMDD_HHMMSS.csv` - Marks/grades
   - `courses_YYYYMMDD_HHMMSS.csv` - Course information
   - `timetable_YYYYMMDD_HHMMSS.csv` - Timetable
   - `academia_data_YYYYMMDD_HHMMSS.xlsx` - All data in Excel format

## Example Output

```
============================================================
🎓 SRM Academia Data Collector
============================================================

📝 Please enter your SRM Academia credentials:
Email (e.g., sv3814@srmist.edu.in): your-email@srmist.edu.in
Password: ********

📝 Step 1: Getting Access Token...
✅ Access Token: abcd1234efgh5678...

📚 Step 2: Collecting Data...

 📌 Fetching Student Details...
 ✅ Student Details Retrieved
 📌 Fetching Attendance...
 ✅ Attendance Retrieved
 📌 Fetching Marks/Grades...
 ✅ Marks Retrieved
 📌 Fetching Courses...
 ✅ Courses Retrieved
 📌 Fetching TimeTable...
 ✅ TimeTable Retrieved

💾 Step 3: Exporting Data...

 📄 Saving as JSON...
 ✅ Saved: academia_data_20251121_190000.json
 📊 Saving as CSV files...
 ✅ Saved: student_20251121_190000.csv
 ✅ Saved: attendance_20251121_190000.csv
 ✅ Saved: marks_20251121_190000.csv
 ✅ Saved: courses_20251121_190000.csv
 ✅ Saved: timetable_20251121_190000.csv
 📈 Saving as Excel...
 ✅ Saved: academia_data_20251121_190000.xlsx

============================================================
📊 Summary of Collected Data:
============================================================
 • Student: 1 record
 • Attendance: 45 records
 • Marks: 12 records
 • Courses: 8 records
 • Timetable: 30 records

✅ Data collection completed!
============================================================
```

## API Reference

This script uses the Vcademia API:

- **Base URL**: `https://vcademia.api.vishok.tech`
- **Authentication**: Token-based authentication
- **Endpoints**:
  - `/key` - Get access token
  - `/student` - Student details
  - `/attendance` - Attendance records
  - `/marks` - Marks/grades
  - `/courses` - Course information
  - `/timetable` - Timetable

## Security Notes

- ⚠️ **Never commit your credentials** to version control
- ⚠️ Credentials are requested at runtime and not stored
- ⚠️ Your password is never logged or saved to files
- ✅ All API communication uses HTTPS

## Troubleshooting

### Common Issues

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` |
| `401 Unauthorized` | Check your email and password |
| `Connection Error` | Check your internet connection |
| Empty CSV files | The API might not have data for that category |

### Getting Help

If you encounter issues:

1. Check that all dependencies are installed
2. Verify your SRM Academia credentials
3. Ensure you have an active internet connection
4. Open an issue on GitHub with error details

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool is for personal use only. Always respect the SRM Institute's terms of service and use this tool responsibly. The author is not responsible for any misuse of this tool.

## Credits

- Created by [Siddharth](https://github.com/siddharth-1118)
- Vcademia API by [Vishok](https://vishok.tech)

## Support

If you find this project helpful, please consider giving it a ⭐ on GitHub!
