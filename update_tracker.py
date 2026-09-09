import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def compile_master_portfolio():
    pdf_path = "Cybersecurity_Newbie.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, title="Cybersecurity Newbie Tracker")
    story = []
    
    primary_color = colors.HexColor("#0D1B2A")
    secondary_color = colors.HexColor("#1B263B")
    bg_light = colors.HexColor("#E0E1DD")
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=22, textColor=primary_color, spaceAfter=6)
    h1_style = ParagraphStyle('SectionH1', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=14, textColor=secondary_color, spaceBefore=12, spaceAfter=6)
    body_style = ParagraphStyle('BodyDark', parent=styles['Normal'], fontName='Helvetica', fontSize=10, textColor=colors.HexColor("#212529"), leading=14, spaceAfter=8)
    code_style = ParagraphStyle('TerminalCode', parent=styles['Code'], fontName='Courier', fontSize=9, textColor=colors.HexColor("#F8F9FA"), backColor=colors.HexColor("#212529"), borderPadding=6, spaceBefore=4, spaceAfter=6)
    
    story.append(Paragraph("🛡️ CYBERSECURITY NEWBIE JOURNEY LOG", title_style))
    story.append(Paragraph("<b>Student Profile:</b> Abdoulaye Sidibe | <b>Portfolio:</b> ://substack.com", body_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("📋 COMPLETED LAB TRAINING MODULES", h1_style))
    lab_data = [
        [Paragraph("<b>Lab Phase</b>", body_style), Paragraph("<b>Core Concepts & Commands Deployed</b>", body_style)],
        [Paragraph("Phase 1: Deployment & System Setup", body_style), Paragraph("Bypassed vendor cloud loops via <code>OOBE\\BYPASSNRO</code>. Injected local administrative account credentials via CLI.", body_style)],
        [Paragraph("Phase 2: Network Reconnaissance", body_style), Paragraph("Deployed VirtualBox environments. Utilized Nmap scanning strings (<code>nmap -v -A</code>) to map open host architectures.", body_style)],
        [Paragraph("Phase 3: Defensive Firewalls", body_style), Paragraph("Provisioned package dependencies via <code>apt</code>. Programmed explicit inbound drops and targeted TCP rule allowances on Port 80 via UFW.", body_style)],
        [Paragraph("Phase 4: Dictionary Exploitation", body_style), Paragraph("Unpacked master wordlist datasets via <code>gzip</code>. Deployed automated multi-threaded login assessment strings via <b>Hydra</b>.", body_style)]
    ]
    t1 = Table(lab_data, colWidths=[150, 310])
    t1.setStyle(TableStyle([('BACKGROUND', (0,0), (1,0), bg_light), ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")), ('VALIGN', (0,0), (-1,-1), 'TOP'), ('BOTTOMPADDING', (0,0), (-1,-1), 6)]))
    story.append(t1)
    
    doc.build(story)

if __name__ == "__main__":
    compile_master_portfolio()
