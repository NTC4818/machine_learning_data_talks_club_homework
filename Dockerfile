FROM agrigorev/zoomcamp-model:2025

# Install uv for dependency management
RUN pip install uv

# Copy dependency files
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen

# Copy the  application
COPY 05-deployment/serve_model.py ./app.py

# Expose the port
EXPOSE 8000

# Run the application with uvicorn
CMD ["uv", "run", "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]