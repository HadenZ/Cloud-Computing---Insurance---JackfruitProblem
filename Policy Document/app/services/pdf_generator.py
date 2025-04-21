from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from datetime import datetime

def generate_policy_pdf(policy_data: dict, output_dir: str = "generated_documents") -> str:
    """
    Generates a PDF document for a policy using details from policy_data.
    Saves the PDF to the output_dir and returns the URL to access the PDF.
    
    :param policy_data: Dict with keys like 'id', 'user_id', 'policy_type', 
                        'coverage_amount', 'premium', 'start_date', 'end_date'
    :param output_dir: Directory where the PDF will be saved.
    :return: URL pointing to the generated PDF.
    """
    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Create a unique filename using the policy ID and current timestamp
    timestamp = int(datetime.utcnow().timestamp())
    filename = f"policy_{policy_data['id']}_{timestamp}.pdf"
    filepath = os.path.join(output_dir, filename)
    
    # Create the PDF using ReportLab
    c = canvas.Canvas(filepath, pagesize=letter)
    width, height = letter
    
    # Write title and policy details
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "Insurance Policy Certificate")
    
    c.setFont("Helvetica", 12)
    text_lines = [
        f"Policy ID: {policy_data.get('id')}",
        f"User ID: {policy_data.get('user_id')}",
        f"Policy Type: {policy_data.get('policy_type')}",
        f"Coverage Amount: {policy_data.get('coverage_amount')}",
        f"Premium: {policy_data.get('premium')}",
        f"Start Date: {policy_data.get('start_date')}",
        f"End Date: {policy_data.get('end_date')}",
        "Thank you for choosing our services."
    ]
    
    y = height - 100
    for line in text_lines:
        c.drawString(50, y, line)
        y -= 20
        
    c.showPage()
    c.save()

    # Construct the URL.
    # You may adjust the host and port as necessary.
    base_url = "http://host.docker.internal:8004/documents"
    generated_url = f"{base_url}/{filename}"
    
    return generated_url
