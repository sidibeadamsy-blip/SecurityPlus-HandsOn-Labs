import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_security_log():
    pdf_path = "The_Cybersecurity_Penetration_Log.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, leftMargin=36, rightMargin=36, topMargin=36, bottomMargin=36)
    story = []
    
    primary_color = colors.HexColor("#0F172A")
    secondary_color = colors.HexColor("#334155")
    bg_table_header = colors.HexColor("#F1F5F9")
    code_bg = colors.HexColor("#F8FAFC")
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('DocTitle', fontName='Helvetica-Bold', fontSize=16, leading=20, textColor=primary_color, spaceAfter=4)
    sub_style = ParagraphStyle('DocSub', fontName='Helvetica-Oblique', fontSize=9.5, leading=13, textColor=secondary_color, spaceAfter=12)
    h1_style = ParagraphStyle('SectionH1', fontName='Helvetica-Bold', fontSize=12, leading=16, textColor=primary_color, spaceBefore=10, spaceAfter=6)
    body_style = ParagraphStyle('BodyDark', fontName='Helvetica', fontSize=9, leading=12, textColor=primary_color)
    header_text_style = ParagraphStyle('HeaderText', fontName='Helvetica-Bold', fontSize=9, leading=12, textColor=primary_color)
    code_style = ParagraphStyle('CodeBox', fontName='Courier', fontSize=8, leading=11, textColor=primary_color, backColor=code_bg, borderPadding=5, spaceBefore=3, spaceAfter=3)
    
    story.append(Paragraph("THE CYBERSECURITY PENETRATION LOG: OPERATIONS ARCHIVE", title_style))
    story.append(Paragraph("<b>Security Analyst:</b> Abdoulaye Sidibe | <b>Specialization:</b> Defensive Auditing", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("A unified operational log capturing hands-on training, network footprinting, and perimeter firewall interface remediation across Linux and automated security environments.", sub_style))
    
    story.append(Paragraph("SECURITY AUDITING ARCHIVE", h1_style))
    
    fixed_widths = [55, 105, 380]
    
    data = [
        [Paragraph("<b>Target ID</b>", header_text_style), Paragraph("<b>Audit Method</b>", header_text_style), Paragraph("<b>CLI vs. GUI Penetration &amp; Footprinting Methodology</b>", header_text_style)],
        [Paragraph("SEC-001", body_style), Paragraph("Network Layer Triage<br/>(Linux DHCP Warmup)", body_style), Paragraph("<b>Remediation:</b> Simulated a network interface link failure on a Linux system. Used administrative tools to force-release the interface configuration lease via <code>dhclient -r</code>, cleared the network footprint, and successfully re-initialized the discovery protocol mapping via <code>dhclient eth0</code> to restore routing connectivity.", body_style)],
        [Paragraph("SEC-002", body_style), Paragraph("Local Footprinting<br/>(Nmap Recon)", body_style), Paragraph("<b>CLI Path:</b> Executed local loopback host reconnaissance natively inside Kali Linux via <code>nmap -sV 127.0.0.1</code> to analyze running daemon version controls and verify network service hardening boundaries.<br/><b>GUI Path:</b> Deployed the graphical Zenmap software interface window, inputting the target node parameter directly into the Target bar and selecting an Intense Scan execution profile loop.", body_style)],
        [Paragraph("SEC-003", body_style), Paragraph("Host Hardening<br/>(Port Filtering)", body_style), Paragraph("<b>CLI Path:</b> Fortified Windows Server 2022 perimeter defenses against lateral movement ransomware vectors. Loaded security dependencies via <code>Import-Module NetSecurity</code>, then deployed an inbound filtering rule targeting TCP Port 445 (SMB) via <code>New-NetFirewallRule</code> to completely drop scanning traffic with a verified baseline status of Block True.", body_style)],
        [Paragraph("SEC-004", body_style), Paragraph("Incident Response<br/>(Host Containment)", body_style), Paragraph("<b>CLI Path:</b> Enforced live threat mitigation inside a virtual infrastructure node. Deployed an out-of-band inbound firewall isolation block targeting a suspected hostile remote host address (<code>192.168.1.99</code>) using the <code>New-NetFirewallRule -RemoteAddress</code> cmdlet to forcefully drop all unauthorized packet ingestion streams.", body_style)]
    ]
    
    t1 = Table(data, colWidths=fixed_widths)
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), bg_table_header),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t1)
    
    story.append(Paragraph("💻 COMMAND INFRASTRUCTURE DEPLOYED:", h1_style))
    story.append(Paragraph("<b>[Host Firewall Port Lockdown]</b> New-NetFirewallRule -DisplayName 'LAB_Block_SMB_Malware' -Direction Inbound -LocalPort 445 -Protocol TCP -Action Block", code_style))
    story.append(Paragraph("<b>[Host Firewall Host Containment]</b> New-NetFirewallRule -DisplayName 'LAB_Block_Rogue_Attacker' -Direction Inbound -RemoteAddress '192.168.1.99' -Action Block", code_style))
    
    doc.build(story)

if __name__ == "__main__":
    generate_security_log()
