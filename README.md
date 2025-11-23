# Kubernetes CI/CD Demo (GitHub Actions + Argo CD)


## Prereqs (local)
- Docker Desktop or Minikube (kubectl working)
- Argo CD
- A GitHub repo with two secrets:
  - `DOCKER_USER`
  - `DOCKER_PASS`

## Local Development

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Locally
```bash
python app/main.py
```

### Run Tests
```bash
pytest
```


## 1) Install Argo CD locally
```bash
kubectl create ns argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl -n argocd port-forward svc/argocd-server 8080:443
# login password
kubectl -n argocd get secret argocd-initial-admin-secret -o jsonpath="{.data.password}" | base64 -d
```

## 2) Create your GitHub repo
- Push this folder to a repo named, e.g., `k8s-cicd-demo`
- Add GitHub repo *Secrets*: `DOCKER_USER`, `DOCKER_PASS`

## 3) Fix image repository in values.yaml (first commit only)
Replace `REPLACE_WITH_YOUR_DOCKERHUB_USERNAME` with your Docker Hub username in `helm/values.yaml`.
(Or let the Action do it on first push via the sed step.)

## 4) Create Argo CD application
In Argo UI → NEW APP:

| Field | Value |
|------|-------|
| Name | demoapp |
| Project | default |
| Sync Policy | Automatic |
| Repo URL | https://github.com/<you>/k8s-cicd-demo |
| Target Revision | manifests |
| Path | helm/ |
| Cluster | https://kubernetes.default.svc |
| Namespace | demo |

```bash
kubectl create ns demo
```

## 5) Run the demo
- Open the app:
  ```bash
  kubectl -n demo port-forward svc/demoapp 8081:80
  # Visit http://localhost:8081
  ```

- Edit `app/main.py` → change the text → commit & push
- Watch GitHub Actions build and push image
- Argo CD auto-syncs and deploys the new verson
- Refresh browser → see the new message 🎉

## Rollback
Use the Argo CD UI to roll back to a previous revision.

---

**Tip:** If your cluster needs an image pull secret, add it to the `demo` namespace and reference it in the deployment template.
# trigger build
