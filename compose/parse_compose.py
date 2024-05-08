# Root: Docker Compose File
    # Branch: version
    #   Leaf: '3.8'
    # Branch: services
    #   Sub-branch: webapp
    #       Leaf: image: webapp:latest
    #       Branch: ports
    #           Leaf: "5000:5000"
    #       Branch: depends_on
    #           Leaf: db
    #   Sub-branch: db
    #       Leaf: image: postgres:12
    #       Branch: volumes
    #           Leaf: db-data:/var/lib/postgresql/data
    # Branch: volumes
    #   Leaf: db-data