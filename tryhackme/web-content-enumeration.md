# Web Content Enumeration (TryHackMe)

## Objective
Understand how attackers discover hidden or unlinked web pages and directories by systematically testing potential resource names on a web application.

## Overview
This exercise focused on identifying exposed web content that is not directly accessible through normal navigation. The lab demonstrated how attackers map an application's attack surface to uncover functionality that may be improperly secured.

## Key Concepts Learned
- Web applications often contain hidden or unlinked pages and directories
- Attackers use enumeration techniques to discover these resources
- Exposed endpoints can reveal sensitive or unauthorized functionality
- Security through obscurity is not an effective defense

## Attacker Perspective (High Level)
- Analyze a web application beyond visible links
- Systematically probe for additional reachable resources
- Identify functionality that should require authorization
- Abuse exposed functionality to perform unintended actions

## Defender Perspective
From a defensive standpoint, this exercise highlights the importance of:
- Enforcing authentication and authorization on all sensitive endpoints
- Validating access server-side, not relying on hidden URLs
- Monitoring for automated or high-volume web requests
- Logging and alerting on abnormal application behavior

## Security Takeaway
Any publicly reachable web resource should be assumed discoverable by attackers. Proper access controls and monitoring must be applied consistently across the entire application, not just visible pages.

## Interview-Ready Summary
This exercise demonstrated how attackers enumerate web applications to uncover hidden functionality and why defenders must enforce strict access controls and monitor for abnormal web activity to prevent unauthorized actions.
