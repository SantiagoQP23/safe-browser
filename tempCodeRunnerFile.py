 url = info_ip["hostname"]

            if url is not None:
              print("Analizando: " + url)

              res = analyze_url(url)
        
              print(res)

              urlService.save_url(url, res)

              print("--------------------------------------------")
