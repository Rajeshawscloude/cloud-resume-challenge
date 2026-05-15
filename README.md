# Cloud Resume Challenge ☁️

## 🌐 Live Website
[http://rajesh-resume-websit.s3-website-us-east-1.amazonaws.com/]

## Overview
Personal resume website built and deployed on AWS
using serverless architecture with live visitor counter.

## Architecture
Browser → CloudFront → S3 (HTML Resume)
                ↓
        API Gateway → Lambda → DynamoDB
        (Live visitor counter!)

## AWS Services Used
- S3 — Host resume HTML file
- CloudFront — HTTPS + fast global delivery
- Lambda — Serverless visitor counter (Python)
- DynamoDB — Store visitor count
- API Gateway — REST API endpoint

## Features
- Professional resume website
- Live visitor counter
- HTTPS secure
- Fast global delivery via CloudFront CDN
- 100% Serverless — no servers to manage!

## How It Works
1. Resume hosted on S3 as static website
2. CloudFront delivers content globally with HTTPS
3. JavaScript calls API Gateway endpoint
4. Lambda function reads/updates DynamoDB count
5. Visitor number displays on website in real time
