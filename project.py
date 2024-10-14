import pandas as pd
from fpdf import FPDF

def create_pdf(Company_Name, Required_Skills, More_Info, output_path):
    pdf = FPDF()
    pdf.add_page()

    # Set font
    pdf.set_font("Arial", size=12)

    # Add content
    pdf.cell(200, 10, txt=f"Company_Name: {Company_Name}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Required_Skills: {Required_Skills}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"More_Info: {More_Info}", ln=True, align='L')

    # Add company seal
    # pdf.image(seal_path, x=10, y=40, w=50)  # Adjust position and size as needed

    # Save the PDF
    pdf.output(output_path)

# Main function
def main():
    csv_file = 'data.csv'  # Path to your CSV file
    # seal_path = 'seal.png'  # Path to your company seal
    output_folder = 'project_final'  # Folder where PDFs will be saved

    # Read CSV data
    data = pd.read_csv(csv_file)

    # Create PDFs for each row in the CSV
    for index, row in data.iterrows():
        Company_Name = row['Company_Name']
        Required_Skills = row['Required_Skills']
        More_Info = row['More_Info']
        output_path = f"{output_folder}{Company_Name.replace(' ', '_')}_certificate.pdf"
        
        create_pdf(Company_Name, Required_Skills, More_Info,output_path)
        # print(f"Generated PDF for {Company_Name}")

if __name__ == "__main__":
    main()