# pycentral

## Introduction

Welcome to the pycentral, a Python SDK for interacting with HPE Aruba Networking Central via REST APIs. This library provides tools for automating repetitive tasks, configuring multiple devices, monitoring, and more.

## HPE Aruba Networking Central Python Package SDK (New Central)

This pre-release allows users to make REST API calls to New Central, the next generation of HPE Aruba Networking Central. It also supports making REST API calls to HPE GreenLake Platform. 
> [!NOTE]
> Upgrading to this pre-release version will not break pycentral-v1 code. All the pycentral-v1 code has been moved to the `classic` folder within pycentral folder, ensuring backward compatibility.

### Installing the Pre-release

To install the pre-release version of pycentral, use the following command:

```bash
pip3 install pycentral==2.0.0b1
```

#### Upgrading to the Pre-release

If you already have pycentral and would like to upgrade to the pre-release version, use the following command:

```bash
pip3 install --upgrade pycentral==2.0.0b1
```

### Getting Started

Once you have installed the pre-release version of pycentral, you need to obtain the necessary authentication details based on the platform you are working with:
1. New Central Authentication
   For New Central, you must obtain the following details before making the API requests:
   1. **Base URL**: This is the API Gateway URL for your New Central account based on the geographical cluster of your account on HPE GreenLake Platform. You can find the base URL of your New Central account's API Gateway from the table [here](https://developer.arubanetworks.com/new-hpe-anw-central/docs/getting-started-with-rest-apis#base-urls).
   2. **Client ID and Client Secret**: These credentials are required to generate an access token to authenticate API requests. You can obtain them by creating a Personal API Client for your New Central Account. Follow the detailed steps in the [Create Client Credentials documentation](https://developer.arubanetworks.com/new-hpe-anw-central/docs/generating-and-managing-access-tokens#create-client-credentials).
2. HPE GreenLake (GLP) Authentication
   If you are working with HPE GreenLake APIs, authentication is slightly different:
   1. GLP does not require a Base URL.
   2. You only need the **Client ID & Client Secret** for the HPE GreenLake Platform.

#### Example Script
Once you have the required credentials, you can initialize the `NewCentralBase` class as follows:
```python
# New Central Import
from pycentral import NewCentralBase


token_info = {
    "glp": {
        "client_id": "<client-id>",
        "client_secret": "<client-secret>",
    },
    "new_central": {
        "base_url": "<api-base-url>",
        "client_id": "<client-id>",
        "client_secret": "<client-secret",
    },
}


new_central_conn = NewCentralBase(
    token_info=token_info,
)

# New Central API Call
new_central_resp = new_central_conn.command(
    api_method="GET", api_path="network-monitoring/v1alpha1/aps"
)

print(new_central_resp)

# GLP API Call
glp_resp = new_central_conn.command(
    api_method="GET", api_path="devices/v1/devices", app_name="glp"
)

print(glp_resp)

```

## Aruba Central Python Package Index SDK (Classic Central)

Aruba Central is an unified cloud-based network management and configuration platform for campus, branch, remote and data center networks. There are various needs for automation and programmability like automating repetitive tasks, configuring multiple devices, monitoring and more. This python package is to programmatically interact with Aruba Central via REST APIs.

### How To Install

In order to run the workflow scripts, please complete the steps below:

1. install virtual env (refer https://docs.python.org/3/library/venv.html). Make sure python version 3 is installed in system.

   ```
   $ python3 -m venv centralenv
   ```

2. Activate the virtual env

   ```
   $ source centralenv/bin/activate
   in Windows:
   $ centralenv/Scripts/activate.bat
   ```

3. Install the **pycentral** package

   ```
   (centralenv)$ pip3 install pycentral
   ```

   To install package with _extras_ `colorLog` which will display log in color

   ```
   (centralenv)$ pip3 install pycentral[colorLog]
   ```

Now you can start making your script based on modules in pycentral or use different workflows from the subpackage `workflows`.

## Executing Scripts

1. Gathering variables required for the package base class `ArubaCentralBase`.

   - **base_url** OR **cluster_name**: You can find the base URL or cluster name of the Central account's API Gateway from the table <a href="https://www.arubanetworks.com/techdocs/central/latest/content/nms/api/domain_url.htm" target="_blank">here</a>. The base URL or cluster name is based on the geographical Central cluster in which the account is registered.

   - **access_token**: You can create an API access token for Aruba Central from -

     - <a href="https://developer.arubanetworks.com/aruba-central/docs/api-gateway-obtaining-access-tokens#obtain-access-token-via-web-ui" target="_blank">Aruba Central UI</a>
     - <a href="https://developer.arubanetworks.com/aruba-central/docs/api-oauth-access-token" target="_blank">OAuth APIs</a>

   - Optional variables - You need to provide the below variables if you want to use PyCentral's ability to generate access tokens from Aruba Central with the help of OAuth APIs.

     - **username** and **password**: Aruba Central user's _username_ and _password_. The access token generated by the OAUTH APIs will have the same role/privileges as the provided Aruba Central user.

     - **client_id** and **client_secret**: Obtain client_id and client_secret variables by creating an API Gateway client in Aruba Central. Refer the following <a href="https://developer.arubanetworks.com/aruba-central/docs/api-gateway-creating-application-token" target="_blank">documentation</a> for more details.

     - **customer_id**: Obtain the **customer_id** by clicking on the figure icon on top right corner of Aruba Central WebUI.

   ![Customer ID](https://github.com/aruba/pycentral/raw/master/pictures/customer-id.png)

2. Providing input variables to the Python scripts. One of the following options can be used.

   - Provide variables directly to Aruba Central Base class in dictionary format.

     Access token approach:

     ```python
     central_info = {
         "base_url": "<api-gateway-domain-url>",
         "token": {
             "access_token": "<api-gateway-access-token>"
         }
     }
     ```

     OAUTH APIs approach with capability to generate new access token:

     ```python
         central_info = {
             "username": "<aruba-central-account-username>",
             "password": "<aruba-central-account-password>",
             "client_id": "<api-gateway-client-id>",
             "client_secret": "<api-gateway-client-secret>",
             "customer_id": "<aruba-central-customer-id>",
             "base_url": "<api-gateway-domain-url>"
         }
     ```

     Alternatively, you can use **cluster_name** instead of **base_url** in the above mentioned dictionaries. You can find the list of clusters that are supported in the <a href="https://github.com/aruba/pycentral/blob/master/pycentral/constants.py" target="_blank">constants.py file</a>. If you would like to add support for other Central clusters, you can do so by adding it in the constants.py.
     Refer the sample scripts in _step3_ and _step4_ for examples.

   - **OR** Provide the required variables using JSON/YAML file. Refer to the sample input files to understand how the files have to be structured -

     - <a href="https://github.com/aruba/pycentral/blob/master/sample_scripts/input_token_only.yaml" target="_blank">sample_scripts/input_token_only.yaml</a>
     - <a href="https://github.com/aruba/pycentral/blob/master/sample_scripts/input_credentials.yaml" target="_blank">sample_scripts/input_credentials.yaml</a>
     - <a href="https://github.com/aruba/pycentral/blob/master/sample_scripts/sample_scripts/input_token_only_cluster.yaml" target="_blank">sample_scripts/input_token_only_cluster_name.yaml</a>
     - <a href="https://github.com/aruba/pycentral/blob/master/sample_scripts/sample_scripts/input_credentials_cluster_name.yaml" target="_blank">sample_scripts/input_credentials_cluster_name.yaml</a>

       More sample input files can be found in the <a href="https://github.com/aruba/pycentral/blob/master/sample_scripts/sample_scripts/" target="_blank">sample_scripts folder</a>. Use `pycentral.workflows_utils.get_conn_from_file()` function which accepts name of the file and returns
       the `ArubaCentralBase` instance object.

3. **Making API call using pycentral base**: Using the base class `ArubaCentralBase`, any Aruba Central supported REST API calls can be made. Refer the following sample script <a href="https://github.com/aruba/pycentral/blob/master/sample_scripts/pycentral_base_sample.py" target="_blank">sample_scripts/pycentral_base_sample.py</a>

   Obtain the HTTP Request related information from Aruba Central Swagger documentation or <a href="https://developer.arubanetworks.com/aruba-central/reference" target="_blank">API references</a> page in Aruba Developer Hub.

4. **Making API call using pycentral modules**: Some API endpoints supported by Aruba Central are implemented as modules in the Python package. Refer the following sample script using modules <a href="https://github.com/aruba/pycentral/blob/master/sample_scripts/pycentral_module_sample.py" target="_blank">sample_scripts/pycentral_module_sample.py</a>

   To obtain a list of implemented modules and its documentation refer the <a href="https://pycentral.readthedocs.io/en/latest/" target="_blank">pycentral module documentation</a>

5. **Workflows**: Workflows are used to achieve an automation use-case which generally involves multiple API calls or dealing with scale and repetitive tasks with ease. Check out the <a href="https://github.com/aruba/central-python-workflows" target="_blank"> central-python-workflows </a> repository to check out workflows that utilize the Pycentral library.

## Documentation:

- **Python package documentation:**
- <a href="https://pycentral.readthedocs.io/en/latest/" target="_blank">pycentral module documentation</a>
- **Use-Cases and Workflows:**
  - <a href="https://developer.arubanetworks.com/aruba-central/docs/python-getting-started" target="_blank">Aruba Developer Hub</a>
  - <a href="https://github.com/aruba/central-python-workflows" target="_blank">central-python-workflows</a>

## Note:

The package takes one of the two approaches to gain access to Aruba Central APIs.

- **OAUTH APIs:** By taking OAUTH approach to generate new access_token, the python package will cache the tokens locally for re-use. Caching tokens locally, helps preventing creation of new access_token every time the script is run. In addition, when the access_token is expired the script will attempt to use the supplied credentials and attempt to refresh the expired token.

  Override the `ArubaCentralBase.storeToken()` and `ArubaCentralBase.loadToken()` function definitions to change this behavior of caching in local file(JSON) and manage tokens more securely.

- **Access Token**: This process is more secure. By providing only the _access_token_ instead of credentials, the package will not cache the tokens. But loses the ability to handle expired token and to generate new access tokens.
