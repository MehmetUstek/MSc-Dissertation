# Configure the AWS provider
provider "aws" {
  region = "us-west-2"
}

resource "aws_api_gateway_domain_name" "as" {
  security_policy = "TLS_1_0"
}

 resource "aws_launch_configuration" "bad_example" {
  associate_public_ip_address = true
    root_block_device {
        encrypted = false
    }
 }

  resource "aws_docdb_cluster" "bad_example" {
   cluster_identifier      = "my-docdb-cluster"
   engine                  = "docdb"
   master_username         = "foo"
   master_password         = "mustbeeightchars"
   backup_retention_period = 5
   preferred_backup_window = "07:00-09:00"
   skip_final_snapshot     = true
   storage_encrypted = false
 }

 
 resource "aws_instance" "bad_example" {
  ami = "ami-7f89a64f"
  instance_type = "t1.micro"

  root_block_device {
      encrypted = false
  }

  ebs_block_device {
    device_name = "/dev/sdg"
    volume_size = 5
    volume_type = "gp2"
    delete_on_termination = false
    encrypted = false
  }
}

 resource "aws_network_acl_rule" "bad_example" {
   egress         = false
   protocol       = "all"
   rule_action    = "allow"
   cidr_block     = "0.0.0.0/0"
 }

// Bu olmadı
 resource "aws_security_group" "bad_example" {
    egress {
        cidr_blocks = ["0.0.0.0/0"]
    }
 }



 resource "aws_default_vpc" "default" {
    tags = {
      Name = "Default VPC"
    }
   }


resource "aws_cloudfront_distribution" "bad_example" {
  default_cache_behavior {
      viewer_protocol_policy = "allow-all"
    }
}

 resource "aws_ebs_volume" "bad_example" {
   availability_zone = "us-west-2a"
   size              = 40

   tags = {
     Name = "HelloWorld"
   }
   encrypted = false
 }


 resource "aws_subnet" "bad_example" {
    vpc_id                  = "vpc-123456"
    map_public_ip_on_launch = true
 }
 
 resource "aws_ecr_repository" "bad_example" {
   name                 = "bar"
   image_tag_mutability = "MUTABLE"

   image_scanning_configuration {
     scan_on_push = false
   }
 }

 resource "aws_efs_file_system" "bad_example" {
   name       = "bar"
   encrypted  = false
   kms_key_id = ""
 }

  resource "aws_elasticsearch_domain" "bad_example" {
   domain_name = "domain-foo"

   encrypt_at_rest {
     enabled = false
   }
 }

  resource "aws_elasticsearch_domain" "bad_example" {
   domain_name = "domain-foo"

   node_to_node_encryption {
     enabled = false
   }
 }

  resource "aws_elasticsearch_domain" "bad_example" {
   domain_name = "domain-foo"

   domain_endpoint_options {
     enforce_https = false
   }
 }




 resource "aws_eks_cluster" "bad_example" {
     // other config 

     name = "bad_example_cluster"
     role_arn = var.cluster_arn
     vpc_config {
        endpoint_public_access = true
        public_access_cidrs = ["0.0.0.0/0"]
     }
 }



 resource "aws_docdb_cluster" "good_example" {
   cluster_identifier      = "my-docdb-cluster"
   engine                  = "docdb"
   master_username         = "foo"
   master_password         = "mustbeeightchars"
   backup_retention_period = 5
   preferred_backup_window = "07:00-09:00"
   skip_final_snapshot     = true
   enabled_cloudwatch_logs_exports = "audit"
 }


 resource "aws_cloudfront_distribution" "bad_example" {
   viewer_certificate {
     cloudfront_default_certificate = aws_acm_certificate.example.arn
     minimum_protocol_version = "TLSv1.0"
   }
 }




# Create a new VPC security group
resource "aws_security_group" "example" {
  name        = "terraform-example-instance"
  description = "Allow SSH inbound traffic"

  # SSH access from anywhere
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

# Create a new AWS EC2 instance
resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1f0" # Update this to the latest Amazon Linux AMI for your region
  instance_type = "t2.micro"
  security_groups = [aws_security_group.example.name]

  tags = {
    Name = "ExampleInstance"
  }
}


 resource "aws_elasticsearch_domain" "good_example" {
   domain_name = "domain-foo"

   domain_endpoint_options {
     enforce_https = true
     tls_security_policy = "Policy-Min-TLS-1-0-2019-07"
   }
 }

 resource "aws_elasticache_replication_group" "bad_example" {
         replication_group_id = "foo"
         replication_group_description = "my foo cluster"

         at_rest_encryption_enabled = false
 }

 resource "aws_alb" "bad_example" {
    internal = false
 }

 resource "aws_elasticache_replication_group" "bad_example" {
         replication_group_id = "foo"
         replication_group_description = "my foo cluster"
         transit_encryption_enabled = false
 }


 resource "aws_alb" "bad_example" {
    name               = "bad_alb"
    internal           = false
    load_balancer_type = "application"

    access_logs {
      bucket  = aws_s3_bucket.lb_logs.bucket
      prefix  = "test-lb"
      enabled = true
    }

    drop_invalid_header_fields = false
   }
 resource "aws_alb_listener" "bad_example" {
    protocol = "HTTP"
 }

resource "aws_iam_access_key" "bad_example" {
    user = "root"
}

 resource "aws_kms_key" "bad_example" {
    enable_key_rotation = false
 }
