import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def create_cybersecurity_newbie_pdf():
    os.makedirs('generated', exist_ok=True)
    pdf_path = "generated/Cybersecurity_Newbie.pdf"
    
    # Initialize Document with strict title compliance
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, title="Cybersecurity Newbie Tracker")
    story = []
    
    # Theme Base Palette
    primary_color = colors.HexColor("#0D1B2A")
    secondary_color = colors.HexColor("#1B263B")
    accent_color = colors.HexColor("#00B4D8")
    bg_light = colors.HexColor("#E0E1DD")
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=24,
        textColor=primary_color,
        spaceAfter=6
    )
    
    h1_style = ParagraphStyle(
        'SectionH1',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=15,
        textColor=secondary_color,
        spaceBefore=14,
        spaceAfter=6
    )
    
    body_style = ParagraphStyle(
        'BodyDark',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        textColor=colors.HexColor("#212529"),
        leading=14,
        spaceAfter=8
    )
    
    code_style = ParagraphStyle(
        'TerminalCode',
        parent=styles['Code'],
        fontName='Courier',
        fontSize=9,
        textColor=colors.HexColor("#F8F9FA"),
        backColor=colors.HexColor("#212529"),
        borderPadding=6,
        spaceBefore=4,
        spaceAfter=6
    )
    
    # Header Elements
    story.append(Paragraph("🛡️ CYBERSECURITY NEWBIE JOURNEY LOG", title_style))
    story.append(Paragraph("<b>Student Profile:</b> Abdoulaye Sidibe (adamsy) | <b>Lab Platform:</b> HP Z440 Workstation (Intel Xeon, 64GB RAM, 512GB SSD)", body_style))
    story.append(Spacer(1, 10))
    
    # SESSION 1 MATRIX
    story.append(Paragraph("📋 SESSION 1: Physical Assembly & Directory Triage", h1_style))
    session1_data = [
        [Paragraph("<b>Topic / Skill Mastered</b>", body_style), Paragraph("<b>Technical Definition & Real-world Application</b>", body_style)],
        [Paragraph("SATA SSD Installation", body_style), Paragraph("Physically mounting and securing internal flash memory onto system rails for fast read/write speeds.", body_style)],
        [Paragraph("Active vs. Passive Video Signals", body_style), Paragraph("Using cables with built-in hardware conversion microchips to manually translate network data streams for mismatched display ports.", body_style)],
        [Paragraph("Directory Navigation (`cd`)", body_style), Paragraph("Command Line tracking mechanics used to route the operating terminal directly into deep system subfolders.", body_style)]
    ]
    t1 = Table(session1_data, colWidths=[150, 350])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (1,0), bg_light),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CCCCCC")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t1)
    story.append(Spacer(1, 12))
    
    # SESSION 2 MATRIX
    story.append(Paragraph("🔒 SESSION 2: Enterprise Bypass, Virtualization & Mapping", h1_style))
    
    story.append(Paragraph("<b>1. The Windows Autopilot/OOBE Override Challenge</b>", body_style))
    story.append(Paragraph("When refurbished hardware retains old enterprise deployment hashes, the machine calls home to cloud configuration matrices. To cut the network dependency and enforce local admin creation, specialized out-of-box commands are required:", body_style))
    story.append(Paragraph("OOBE\BYPASSNRO", code_style))
    
    story.append(Paragraph("<b>2. Administrative Account Injections</b>", body_style))
    story.append(Paragraph("Forcefully breaking into the operating environment requires injecting custom accounts straight into the master local security groups database via terminal nodes:", body_style))
    story.append(Paragraph("net user adamsy /add<br/>net localgroup administrators adamsy /add", code_style))
    
    story.append(Paragraph("<b>3. Network Footprinting & Target Reconnaissance (Nmap)</b>", body_style))
    story.append(Paragraph("Using Network Mapper configurations to safely perform remote footprint scans, discovering open port matrices, active transport protocols, and target Operating System structures:", body_style))
    story.append(Paragraph("sudo nmap -v -A scanme.nmap.org", code_style))
    
    # Safe Medical/Informational Footer Disclaimer
    story.append(Spacer(1, 20))
    story.append(Paragraph("<font size=7 color='#6C757D'>This is for informational purposes only. For medical advice or diagnosis, consult a professional. AI responses may include mistakes.</font>", body_style))
    
    doc.build(story)

create_cybersecurity_newbie_pdf()
