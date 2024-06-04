import pandas as pd

# Create a dictionary with some data
data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 40, 35],
    'city': ['New York', 'Los Angeles', 'San Francisco']
}

# Convert the dictionary into a DataFrame
df = pd.DataFrame(data)

# Output the DataFrame
print(df)



# Set the file path and name for the SSH key
$keyPath = "C:\Users\ASUS\bryanjomondi\.ssh\id_rsa"

# Create the .ssh directory if it doesn't exist
$sshDirectory = Split-Path -Path $keyPath
if (-not (Test-Path -Path $sshDirectory)) {
    New-Item -ItemType Directory -Path $sshDirectory | Out-Null
}

# Generate the SSH key pair
ssh-keygen -t rsa -b 4096 -f $keyPath -N ""

# Display the public key
Write-Host "Public Key:"
Get-Content -Path "$keyPath.pub"

