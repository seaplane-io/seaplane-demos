import requests
import json

def get_all_pages(headers):
    """ Get all pages our integration has access to 

    Keyword arguements:
    headers -- a headers JSON object:
        Authorization': f"Bearer {NOTION_KEY}", 
           'Content-Type': 'application/json', 
           'Notion-Version': '2022-06-28
    """

    # set API search parameters
    search_params = {"filter": {"value": "page", "property": "object"}}

    # initialize with has more true and empty list for all results
    has_more = True
    all_results = []
    data= {}

    # loop through pagination
    while has_more == True:  
        # request an object of all pages the intregration has access to
        search_response = requests.post(
            f'https://api.notion.com/v1/search', 
            json=search_params, headers=headers, data=json.dumps(data))
        
        # get the current results
        cur_result = search_response.json()

        # check if there are more pages 
        if cur_result['has_more']:
            # set the cursor start position
            data["start_cursor"] = cur_result["next_cursor"]
        else: has_more = False

        all_results.append(cur_result)

    # return all the results
    return all_results

def get_page(created_id, headers):
    """Get and return the page object from the Notion API

    Keyword arguments:
    created_id -- the page id associated with the page
    headers -- a headers JSON object:
        Authorization': f"Bearer {NOTION_KEY}", 
           'Content-Type': 'application/json', 
           'Notion-Version': '2022-06-28
    """

    # get all the block for page associated with created_id
    blocks_response = requests.get(
        f"https://api.notion.com/v1/blocks/{created_id}/children", 
        headers=headers)
    
    # return the page blocks
    return blocks_response.json()

def get_page_content(page):
    """ Get the rich text content of a Notion page object

    Keyword arguments:
    page -- a notion page object JSON
    """
    # string to store the page content of current page
    page_content = ""

    # loop through all blocks and try to get the page content if it exists
    for i in page['results']:
        type = i["type"]
        try: 
            page_content += i[type]["rich_text"][0]["text"]["content"]
        except:
            # continue if the current block does not contain text
            continue

    # return the page content
    return page_content
