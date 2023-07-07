class Uploader:

    @staticmethod
    def upload_photo_for_students(instance, filename):
        return f"students/{instance.slug}/{filename}"

    @staticmethod
    def upload_photo_for_blog(instance, filename):
        return f"blog/{instance.slug}/{filename}"
