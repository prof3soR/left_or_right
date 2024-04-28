import requests
import os


def download_image(student_number, save_folder="images"):
    try:
        # Construct the URL with the student number
        url = f"https://pay.mvgrce.edu.in/ecap/StudentPhotos/{student_number}.jpg"
        # Send a GET request to the URL
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Create the save folder if it doesn't exist
            if not os.path.exists(save_folder):
                os.makedirs(save_folder)
            # Construct the full path to save the image
            save_path = os.path.join(save_folder, f"{student_number}.jpg")
            # Write the image content to the file
            with open(save_path, "wb") as f:
                f.write(response.content)
            print(f"Image downloaded successfully: {save_path}")
        else:
            print(
                f"Failed to download image for student {student_number}: HTTP status code {response.status_code}")
    except Exception as e:
        print(
            f"An error occurred while downloading image for student {student_number}: {e}")


if __name__ == "__main__":
    student_numbers = [i for i in range(1201, 1299)]
    for number in student_numbers:
        download_image("20331a"+str(number))
