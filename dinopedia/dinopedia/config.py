import os


DATABASE_HOST: str = os.getenv("POSTGRES_HOST", "django-dino.cmpkpzjgafgz.eu-south-1.rds.amazonaws.com")
DATABASE_NAME: str = os.getenv("POSTGRES_DB", "postgres")
DATABASE_PORT: int = os.getenv("POSTGRES_PORT", 5432)
DATABASE_USER: str = os.getenv("POSTGRES_USER", "djangodino")
DATABASE_PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "djangodino1")
SECRET_KEY_DINO: str = os.getenv("SECRET_KEY_DINO",
                                 "django-insecure-aogn%uvt*wpm&llpt%_ryu6$ao&t*%m&id&6b-1ct1qtkzoj3q")
# AWS_STORAGE_BUCKET_NAME: str = os.getenv("AWS_STORAGE_BUCKET_NAME", "django-dino-blog")
# AWS_S3_REGION_NAME: str = os.getenv("AWS_S3_REGION_NAME", "eu-south-1")
# AWS_ACCESS_KEY_ID: str = os.getenv("AWS_ACCESS_KEY_ID", "AKIAVHXBZJPRANPAWU73")
# AWS_SECRET_ACCESS_KEY: str = os.getenv("AWS_SECRET_ACCESS_KEY", "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")

