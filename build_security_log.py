import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_security_log():
    pdf_path = "The_Cybersecurity_Penetration_Log.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, leftMargin=36, rightMargin=36, topMargin=36, bottomMargin=36)
    story = []
    
    primary_color = colors.HexColor("#1E293B")
    secondary_color = colors.HexColor("#475569")
    bg_table_header = colors.HexColor("#E2E8F0")
    code_bg = colors.HexColor("#F1F5F9")
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('DocTitle', fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=primary_color, spaceAfter=6)
    sub_style = ParagraphStyle('DocSub', fontName='Helvetica-Oblique', fontSize=10, leading=14, textColor=secondary_color, spaceAfter=14)
    h1_style = ParagraphStyle('SectionH1', fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=primary_color, spaceBefore=14, spaceAfter=6)
    body_style = ParagraphStyle('BodyDark', fontName='Helvetica', fontSize=9.5, leading=13, textColor=primary_color)
    header_text_style = ParagraphStyle('HeaderText', fontName='Helvetica-Bold', fontSize=9.5, leading=13, textColor=primary_color)
    code_style = ParagraphStyle('CodeBox', fontName='Courier', fontSize=8.5, leading=12, textColor=primary_color, backColor=code_bg, borderPadding=6, spaceBefore=4, spaceAfter=4)
    
    story.append(Paragraph("THE CYBERSECURITY PENETRATION LOG: OPERATIONS ARCHIVE", title_style))
    story.append(Paragraph("<b>Security Analyst:</b> Abdoulaye Sidibe | <b>Specialization:</b> Defensive Auditing", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("A unified operational log capturing hands-on training, network footprinting, and interface remediation across Linux and automated security environments.", sub_style))
    
    story.append(Paragraph("SECURITY AUDITING ARCHIVE", h1_style))
    data = [
        [Paragraph("<b>Target ID</b>", header_text_style), Paragraph("<b>Audit Method</b>", header_text_style), Paragraph("<b>CLI vs. GUI Penetration &amp; Footprinting Methodology</b>", header_text_style)],
        [Paragraph("SEC-001", body_style), Paragraph("Network Layer Triage<br/>(Linux DHCP Warmup)", body_style), Paragraph("<b>Remediation:</b> Simulated a network interface link failure on a Linux system. Used administrative tools to force-release the interface configuration lease via <code>dhclient -r</code>, cleared the network footprint, and successfully re-initialized the discovery protocol mapping via <code>dhclient eth0</code> to restore routing connectivity.", body_style)],
        [Paragraph("SEC-002", body_style), Paragraph("Local Footprinting<br/>(Nmap Recon)", body_style), Paragraph("<b>CLI Path:</b> Executed local loopback host reconnaissance natively inside Kali Linux via <code>nmap -sV 127.0.0.1</code> to analyze running daemon version controls and verify network service hardening boundaries.<br/><br/><b>GUI Path:</b> Deployed the graphical Zenmap software interface window, inputting the target node parameter directly into the <code>Target</code> bar and selecting an <code>Intense Scan</code> execution profile loop.", body_style)]
    ]
    
    # Safely declared table widths using an isolated variable
    table_widths = [60, 110, 370]
    t1 = Table(data, colWidths=table_widths)
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), bg_table_header),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t1)
    
    story.append(Paragraph("COMMAND INFRASTRUCTURE DEPLOYED:", h1_style))
    story.append(Paragraph("<b>[DHCP Blackout Clear]</b><br/>dhclient -r && dhclient eth0", code_style))
    story.append(Paragraph("<b>[CLI Target Recon]</b><br/>nmap -sV 127.0.0.1", code_style))
    story.append(Paragraph("<b>[GUI Navigation Path]</b><br/>Launch Zenmap Application -> Input '127.0.0.1' into Target Field -> Set Profile to 'Intense Scan' -> Click Scan Button", code_style))
    
    doc.build(story)

if __name__ == "__main__":
    generate_security_log()
