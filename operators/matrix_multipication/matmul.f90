function matmul(a, b) result(c)
    implicit none

    real(kind=8), intent(in)    :: a(:,:)
    real(kind=8), intent(in)    :: b(:,:)
    real(kind=8)    :: c(size(a,1),size(b,2))
    real(kind=8)    :: temp
    integer k, l, i, j

    do k= 1, size(a, 1), 1
        do j= 1, size(b, 2), 1
            temp= 0.0d0
            do i= 1, size(b, 2), 1
                temp= temp+ a(k, i)*b(i, j)
            end do
            c(k, j)= temp
        end do
    end do

end function matmul