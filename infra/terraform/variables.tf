# infra/terraform/variables.tf

variable "aws_region" {
  description = "The AWS region to deploy the infrastructure to."
  default     = "us-west-2"
}

variable "vpc_cidr_block" {
  description = "The CIDR block for the VPC."
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr_blocks" {
  description = "The CIDR blocks for the public subnets."
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]
}

variable "private_subnet_cidr_blocks" {
  description = "The CIDR blocks for the private subnets."
  type        = list(string)
  default     = ["10.0.3.0/24", "10.0.4.0/24"]
}

variable "acm_certificate_arn" {
  description = "The ARN of the ACM certificate for the load balancer."
  type        = string
}

variable "image_tag" {
  description = "The tag of the Docker image to deploy."
  type        = string
  default     = "latest"
}
