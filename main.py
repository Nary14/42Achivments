import os
from enum import Enum
from dotenv import load_dotenv
from app import create_app

load_dotenv()


class DeploymentStatus(str, Enum):
    DEV = "development"
    PROD = "production"


if __name__ == "__main__":
    app = create_app()
    host: str = os.getenv("HOST", "0.0.0.0")
    port_str: str = os.getenv("PORT", "5000")
    port: int = int(port_str)

    status_str = os.getenv("DEPLOYMENT_STATUS", DeploymentStatus.PROD.value)
    current_status = DeploymentStatus(status_str)
    is_dev = current_status == DeploymentStatus.DEV
    app.run(debug=is_dev, host=host, port=port)
