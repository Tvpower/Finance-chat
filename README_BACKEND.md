## 🔌 API Endpoints

### POST `/upload/`
Upload and process a PDF document
- **Parameters**: `file` (PDF file)
- **Returns**: Processing status and file path

### POST `/chat/`
Chat with processed documents
- **Parameters**: `query` (string) - Your question
- **Returns**: AI-generated response based on document content

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source. Please check the license file for more details.

## 🆘 Troubleshooting

### Common Issues

1. **Port Already in Use**:
   - Change the port in `main.py` (line with `uvicorn.run`)
   - Or kill the process using the port

2. **Module Not Found Errors**:
   - Ensure your virtual environment is activated
   - Reinstall dependencies: `pip install -r requirements.txt`

3. **PDF Processing Errors**:
   - Ensure the uploaded file is a valid PDF
   - Check file size limitations
   - Verify the PDF contains readable text (not just images)

4. **API Connection Issues**:
   - Ensure both FastAPI backend and Streamlit frontend are running
   - Check that the API URL in `app.py` matches your FastAPI server address

## 📞 Support

If you encounter any issues or have questions, please open an issue in the repository.

---